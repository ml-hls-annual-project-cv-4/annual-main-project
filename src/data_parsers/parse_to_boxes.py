import os
import sys
from src.databases.dwh import DwhDb
import numpy as np
import pandas as pd
from multiprocessing import Pool, cpu_count

def create_table(tblname):
    tables_list = DwhDb().show_tables()
    
    if tblname not in tables_list:
        with DwhDb().def_client() as client:
            client.command(
                f'create table {tblname} ('
                    'name String,'
                    'weather String,'
                    'scene String,'
                    'timeofday String,'
                    'timestamp Int64,'
                    'category String,'
                    'manualShape Bool,'
                    'manualAttributes Bool,'
                    'id Int64,'
                    'attributes_occluded Nullable(String),'
                    'attributes_truncated Nullable(String),'
                    'attributes_trafficLightColor Nullable(String),'
                    'box2d_x1 Nullable(Float64),'
                    'box2d_y1 Nullable(Float64),'
                    'box2d_x2 Nullable(Float64),'
                    'box2d_y2 Nullable(Float64),'
                    'ls_box_img Array(Array(Array(Int32)))'
                ')'
                'engine = MergeTree()'
                'order by (name, id)'
            )
    else:
        print('Table already exists')

def get_img_names_lists(tbl_images, tbl_boxes, img_per_ls):
    with DwhDb().def_client() as client:
        ls_names = client.query_df(
            "select distinct name from {tbl_images: Identifier}",
            parameters={'tbl_images': tbl_images})['name'].tolist()
        
    with DwhDb().def_client() as client:
        df_boxes = client.query_df(
            "select distinct name from {tbl_boxes: Identifier}",
            parameters={'tbl_boxes': tbl_boxes})
        
    if df_boxes.shape[0] != 0:
        ls_names = [i for i in ls_names if i not in df_boxes['name'].tolist()]
        
    res_ls = []
    ls_start = 0
    for i in range(len(ls_names) // img_per_ls + min(1, len(ls_names) % img_per_ls)):
        res_ls.append(ls_names[ls_start:min(ls_start + img_per_ls, len(ls_names))])
        ls_start += img_per_ls
    return res_ls

def cut_box_from_image(df_images, image_name, x1, y1, x2, y2):
    ls_image = df_images[lambda x: x.name == image_name]['img_bgr_row'].tolist()
    ls_box = ls_image[int(np.floor(y1)):int(np.ceil(y2))]
    ls_box = [i[int(np.floor(x1)):int(np.ceil(x2))] for i in ls_box]
    return ls_box

def write_boxes_batch(ls_names_batch):
    df_images = DwhDb().select_by_imgname(ls_names_batch, f'images_{data_batch}')
    df_labels = DwhDb().select_by_imgname(ls_names_batch, f'labels_{data_batch}')
    df_labels = df_labels[[not i for i in pd.isna(df_labels['box2d_x1'])]].iloc[:, 0:16]
    df_labels['ls_box_img'] = df_labels.apply(
        lambda x: cut_box_from_image(df_images, x['name'], x.box2d_x1, x.box2d_y1, x.box2d_x2, x.box2d_y2),
        axis = 1)
    with DwhDb().def_client() as client:
        client.insert_dataframe(f'boxes_{data_batch}', df_labels)

for data_batch in ['train', 'val']:
    create_table(f'boxes_{data_batch}')
    ls_names = get_img_names_lists(f'images_{data_batch}', f'boxes_{data_batch}', 30)
    with Pool(max(1, cpu_count() - 1)) as pool:
        pool.map(write_boxes_batch, ls_names)