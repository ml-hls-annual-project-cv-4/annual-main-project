import src.databases.dwh as dwh

# Default database - cv_project
# Also default user has wrights to write to test db
with dwh.def_client() as client:
    client.execute(
        'show databases'    
    )
    client.execute(
        'show tables'    
    )
    client.execute(
        'use test'    
    )
    client.execute(
        'drop table if exists testidze'    
    )
    client.execute(
        'show tables'    
    )
    client.execute(
        'create table if not exists testidze ('
        'a String,'
        'b Nullable(Int64)'
        ') engine Memory' # not the best engine, read docs
    )
    client.execute(
        'show tables'    
    )
    
# Clickhouse docs https://clickhouse.com/docs/en/home/
# clickhouse_driver docs https://clickhouse-driver.readthedocs.io/en/latest/index.html

    
# When you use def_client with settings={}
# you get result as list
# Be careful with brackets when use strings in where statement
# Only configuration below works
# Also with where statement you should write query in one row
with dwh.def_client(settings={}) as client:
    res_list = client.execute(
        "select * from labels_train where name = '0004974f-05e1c285.jpg'"
    )
res_list

# Using def_client with default settings ({'use_numpy': True})
# and using query_dataframe() instead of execute()
# making it much faster
with dwh.def_client() as client:
    df = client.query_dataframe(
        "select * from labels_val where name = '0004974f-05e1c285.jpg'"
    )
df.info()

# If you don't need any additional conditions
# you can use this syntax
df = dwh.read_dataframe(
    'cv_project',
    'labels_train')
df.info()

# File with connection credentials must be stored in 'databases/dwh_def_user.pickle'
# If you need change something
import pickle

with open('databases/dwh_def_user.pickle', 'rb') as file:
    a = pickle.load(file)

a['host'] = 'some_host' 

with open('databases/dwh_def_user.pickle', 'wb') as file:
    pickle.dump(a, file, protocol=pickle.HIGHEST_PROTOCOL)
    
# Don't forget to add credentials to .gitignore!!!! 