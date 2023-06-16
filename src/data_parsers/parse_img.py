import os
from functools import reduce
from multiprocessing import Pool, cpu_count

import cv2
import pandas as pd

from src.databases.dwh import DwhDb


def create_table(tblname):
    tables_list = DwhDb().show_tables()

    if tblname not in tables_list:
        with DwhDb().def_client() as client:
            client.command(
                f'create table {tblname} ('
                'name String,'
                'row_number Int32,'
                'img_bgr_row Array(Array(Int32))'
                ')'
                'engine = MergeTree()'
                'order by (name, row_number)'
            )
    else:
        print('Table already exists')


def prep_img_names(tbl_images, data_batch, img_per_ls):
    with DwhDb().def_client() as client:
        df_db_images = client.query_df(f"select distinct name from {tbl_images}")
    ls_imgfiles_names = os.listdir(f'datasets/images/{data_batch}/')
    if df_db_images.shape[0] != 0:
        ls_imgfiles_names = [i for i in ls_imgfiles_names if i not in df_db_images['name'].tolist()]
    res_ls = []
    ls_start = 0
    for i in range(len(ls_imgfiles_names) // img_per_ls + min(1, len(ls_imgfiles_names) % img_per_ls)):
        res_ls.append(ls_imgfiles_names[ls_start:min(ls_start + img_per_ls, len(ls_imgfiles_names))])
        ls_start += img_per_ls
    return [res_ls, len(df_db_images)]


def parse_img(img_name, data_batch):
    ls_img = cv2.imread(f'datasets/images/{data_batch}/{img_name}').tolist()
    df_img = pd.DataFrame({'name': img_name,
                           'row_number': [i for i in range(len(ls_img))],
                           'img_bgr_row': ls_img})
    return df_img


def write_img_batch(img_names_batch):
    with DwhDb().def_client() as client:
        client.insert_dataframe(tbl_name,
                                reduce(lambda x, y: pd.concat([x, y]),
                                       map(lambda x: parse_img(x, data_batch=data_batch), img_names_batch)))


for data_batch in os.listdir('datasets/images/'):
    tbl_name = f'images_{data_batch}'
    create_table(tbl_name)
    ls_img_names, db_img_qnt = prep_img_names(tbl_name, data_batch, img_per_ls=30)
    print(f'{db_img_qnt} images already in {data_batch} table')
    with Pool(max(1, cpu_count() - 1)) as pool:
        pool.map(write_img_batch, ls_img_names)
