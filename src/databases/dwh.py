from clickhouse_driver import Client
import pickle
    
def def_client(creds_file='databases/dwh_def_user.pickle',
               settings={'use_numpy': True}):
    """Function returns connection client to dwh interface"""
    
    with open('src/databases/dwh_def_user.pickle', 'rb') as handle:
        def_user_creds = pickle.load(handle)

    client = Client(
        host=def_user_creds['host'],
        user=def_user_creds['user'],
        password=def_user_creds['password'],
        settings=settings)

    return client


def insert_dataframe(dbname, tblname, df, dwh_client=def_client()):
    """Func writes pandas df into db table.
    It's used only with {'use_numpy': True} in client settings"""
    with dwh_client as client:
        client.execute(
            f'use {dbname}'
        )
        client.insert_dataframe(
            f'insert into {tblname} values',
            df
        )


def read_dataframe(dbname, tblname, dwh_client=def_client()):
    """Func reads pandas df from db table.
    It's used only with {'use_numpy': True} in client settings"""
    with dwh_client as client:
        client.execute(
            f'use {dbname}'
        )
        df = client.query_dataframe(
            'select *'
            f'from {tblname}'
        )
    return df

def select_db_labels(ls_names, tbl_name, dbname='cv_project'):
    '''
    Func gets dataframe with metadata corresponding to image names were given as argument ls_names
    '''
    if not isinstance(ls_names, list):
        ls_names = [ls_names,]
    str_names = ', '.join([f"'{i}'" for i in ls_names])
    with def_client() as client:
        client.execute(
            f'use {dbname}'
        )
        df = client.query_dataframe(
            f"select * from {tbl_name} where name in ({str_names})"
        )
    return df

def select_db_images(ls_names, tbl_name):
    '''
    Func gets dataframe with image arrays corresponding to image names were given as argument ls_names
    '''
    if not isinstance(ls_names, list):
        ls_names = [ls_names,]
    str_names = ', '.join([f"'{i}'" for i in ls_names])
    with def_client() as client:
        df = client.query_dataframe(
            f"select * from {tbl_name} where name in ({str_names})"
        )
    return df