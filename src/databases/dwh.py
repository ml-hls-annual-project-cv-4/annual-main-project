# Потом перейдет в нормальный вид в качестве класса вместе со всеми парсерами

#Pickle файл явялется приватным, его надо запрашивать отдельно
def def_client(creds_file='databases/dwh_def_user.pickle',
               settings={'use_numpy': True}):
    """Function returns connection client to dwh interface"""
    from clickhouse_driver import Client
    import pickle

    with open('databases/dwh_def_user.pickle', 'rb') as handle:
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
