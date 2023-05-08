'''

Clickhouse docs https://clickhouse.com/docs/en/home/
clickhouse_connect docs https://clickhouse.com/docs/en/integrations/python

Common querys are gonna be like described below

SELECT
----------------------------------------------------
parameters = {'table': 'boxes_train', 'img_name': ['0000f77c-6257be58.jpg', '0001542f-5ce3cf52.jpg']}
with DwhDb().def_client() as client:
    res = client.query_df('select * from {table: Identifier} where name in {img_name: Array(String)}', 
                          parameters=parameters)
----------------------------------------------------
you can use client.query and get a dictionary instead df

If want to get all table without any conditions feel free to use read_dataframe method:

----------------------------------------------------
res_df = DwhDb().read_dataframe('testidze')
----------------------------------------------------

CREATE TABLE
----------------------------------------------------
with DwhDb().def_client() as client:
    client.command(
        'create table if not exists testidze ( \
            a String, \
            b Nullable(Int64) \
        ) engine Memory' # not the best engine, read docs
    )
----------------------------------------------------

INSERT
----------------------------------------------------
import pandas as pd

some_df = pd.DataFrame({'a': ['sfd'], 'b': [1231]})
DwhDb().insert_dataframe('testidze', some_df)
----------------------------------------------------

'''

import pickle
import clickhouse_connect as ch

class DwhDb:

    def __init__(self, creds_file='databases/dwh_def_user.pickle', database='cv_project'):
        self.creds_file = creds_file
        self.database=database
        
    def def_client(self):
        ''' Function returns connection client object to dwh interface '''
        
        with open('src/databases/dwh_def_user.pickle', 'rb') as handle:
            def_user_creds = pickle.load(handle)

        client = ch.get_client(
            host=def_user_creds['host'],
            username=def_user_creds['user'],
            password=def_user_creds['password'],
            database=self.database
        )

        return client
    
    def show_tables(self):
        ''' Function returns current database tables list '''
        
        with self.def_client() as client:
            tables_list = client.command('show tables')
            
        return tables_list
    
    def insert_dataframe(self, tblname, df):
        ''' Func writes pandas df into db table '''
        
        with self.def_client() as client:
            client.insert_df(
                table=tblname,
                df=df
            )
            
    def read_dataframe(self, tblname):
        ''' Func reads pandas df from db table without any additional conditions '''
        
        with self.def_client() as client:
            df = client.query_df('select * from {tbl: Identifier}', 
                                 parameters={'tbl': tblname})
        return df
    
    def select_by_imgname(self, img_names, tbl_name):
        '''
        Func gets dataframe with data corresponding to image names were given as argument img_names
        '''
        
        if not isinstance(img_names, list):
            img_names = [img_names,]
        
        with self.def_client() as client:
            res = client.query_df(
                'select * from {tbl: Identifier} where name in {img_names: Array(String)}',
                parameters={'tbl': tbl_name, 'img_names': img_names}
            )
            
        return res
        
    pass


if __name__ == '__main__':
    with DwhDb().def_client() as client:
        print(
            'DWH connection has created succesfully!\n' + \
                'List of tables: \n' + \
                    f'{client.command("show tables")}'
        )
