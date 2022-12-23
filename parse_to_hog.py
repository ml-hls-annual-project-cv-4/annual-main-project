import os
import sys
sys.path.append(os.path.abspath("databases/"))
import dwh
import pandas as pd
import numpy as np
from skimage.feature import hog
from multiprocessing import Pool, cpu_count
import cv2

hog_version = ''
img_per_ls = 50

def create_table(tblname):
    with dwh.def_client() as client:
        client.execute(
            'use cv_project'    
        )
        tables_list = client.execute(
            'show tables'
        )
        
    if tblname not in tables_list:
        with dwh.def_client() as client:
            client.execute(
                'use cv_project'
            )
            client.execute(
                f'create table {tblname} ('
                    'name String,'
                    'weather String,'
                    'scene String,'
                    'timeofday String,'
                    'category String,'
                    'id Int64,'
                    'hog Array(Float64)'
                ')'
                'engine = MergeTree()'
                'order by (name, id)'
            )
    else:
        print('Table already exists')

def get_img_names_lists(tbl_boxes, tbl_hog, img_per_ls):
    with dwh.def_client() as client:
        ls_names = client.query_dataframe(f"select distinct name from {tbl_boxes}")['name'].tolist()
    with dwh.def_client() as client:
        ls_hog_names = client.query_dataframe(f"select distinct name from {tbl_hog}")
    if ls_hog_names.shape[0] != 0:
        ls_names = [i for i in ls_names if i not in ls_hog_names['name'].tolist()]
    res_ls = []
    ls_start = 0
    for i in range(len(ls_names) // img_per_ls + min(1, len(ls_names) % img_per_ls)):
        res_ls.append(ls_names[ls_start:min(ls_start + img_per_ls, len(ls_names))])
        ls_start += img_per_ls
    return res_ls

def select_db_boxes(ls_names, tbl_boxes):
    str_names = ', '.join([f"'{i}'" for i in ls_names])
    with dwh.def_client() as client:
        df = client.query_dataframe(
            f"select * from {tbl_boxes} where name in ({str_names})"
        )
    return df

def calc_hog(ls_img, width, height):
    if min(width, height) < 32:
        size = 32
    else :
        size = int(32*2**np.floor(np.log2(min(width, height) // 32)))
    img = cv2.cvtColor(np.array(ls_img, dtype=np.uint8), cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (size, size))    
    return hog(img, orientations=8, pixels_per_cell=(int(size / 8), int(size / 8)), 
               cells_per_block=(2,2), channel_axis = -1, visualize=False)

def write_hog_batch(ls_img_names_batch):
    df_boxes = select_db_boxes(ls_img_names_batch, f'boxes_{data_batch}')
    df_boxes = (df_boxes.assign(width = lambda x: np.ceil(x.box2d_x2) - np.floor(x.box2d_x1))
                        .assign(height = lambda x: np.ceil(x.box2d_y2) - np.floor(x.box2d_y1))
                        .drop(['timestamp', 'manualShape', 'manualAttributes', 
                               'attributes_occluded', 'attributes_truncated', 
                               'attributes_trafficLightColor', 'box2d_x1',
                               'box2d_y1', 'box2d_x2', 'box2d_y2'], axis = 1))
    df_boxes['hog'] = df_boxes.apply(lambda x: calc_hog(ls_img=x.ls_box_img, width=x.width, height=x.height), axis=1)
    df_boxes.drop(['ls_box_img'], axis=1, inplace=True)
    with dwh.def_client() as client:
        client.insert_dataframe(f'insert into hog{hog_version}_{data_batch} values', df_boxes)

for data_batch in ['train', 'val']:
    create_table(f'hog{hog_version}_{data_batch}')
    ls_names = get_img_names_lists(f'boxes_{data_batch}', f'hog{hog_version}_{data_batch}', img_per_ls)
    with Pool(max(1, cpu_count() - 1)) as pool:
        pool.map(write_hog_batch, ls_names)
        