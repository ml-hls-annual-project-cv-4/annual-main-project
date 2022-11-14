import json
import pandas as pd
import sys 
import os
sys.path.append(os.path.abspath("databases/"))
import dwh
        
def parse_one_img (obj_to_parse):
    '''Func that parse piece of json corresponded to one img'''        
    dict = json.loads(obj_to_parse)
    df_name = pd.DataFrame({'name': [dict['name']]})
    df_attributes = pd.json_normalize(dict['attributes']) 
    df_timestamp = pd.DataFrame({'timestamp': [dict['timestamp']]})
    df_labels = pd.concat(
        map(lambda label: pd.json_normalize(label), dict['labels']))
    df = pd.concat([pd.concat([df_name, df_attributes, df_timestamp], axis = 1), 
                    df_labels], axis = 1)
    df.rename(lambda x: x.replace('.', '_'), axis = 1, inplace=True)
    
    for column in ['attributes_truncated', 'attributes_occluded']:
        df[column] = df[column].apply(str)    
    
    for column in ['attributes_areaType', 
                   'poly2d', 
                   'attributes_laneDirection',
                   'attributes_laneStyle',
                   'attributes_laneType']:
        if column not in df.columns:
            df[column] = str('nan')    
    
    for column in ['vertices', 'types', 'closed']:
        df[f'poly2d_{column}'] = df['poly2d'].apply(
            lambda poly2d: str(poly2d[0][column]) if ('list' in str(type(poly2d))) else poly2d)
    
    df.drop('poly2d', axis = 1, inplace=True)
    return df

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
                    'attributes_areaType Nullable(String),'
                    'attributes_laneDirection Nullable(String),'
                    'attributes_laneStyle Nullable(String),'
                    'attributes_laneType Nullable(String),'
                    'poly2d_vertices Nullable(String),'
                    'poly2d_types Nullable(String),'
                    'poly2d_closed Nullable(String)'
                ')'
                'engine = MergeTree()'
                'order by (name, id)'
            )
    else:
        print('Table already exists')

for tblname, filename in [
    ['labels_train', 'bdd100k_labels_images_train.json'],
    ['labels_val', 'bdd100k_labels_images_val.json']]:
    
    create_table(tblname)

    with open(filename) as file:
        brackets_counter = 0
        obj_to_parse = ''
        mode = 'start'
        for row in file.readlines():
            for sym in row:
                if sym == '{':
                    brackets_counter += -1
                    if brackets_counter == -1:
                        mode = 'collect' 
                elif sym == '}':
                    brackets_counter += 1
                    if brackets_counter == 0:
                        obj_to_parse += sym
                        df = parse_one_img(obj_to_parse)
                        dwh.insert_dataframe(dbname='cv_project', 
                                            tblname=tblname, 
                                            df=df) 
                        obj_to_parse=''
                        mode='start'
                if mode == 'collect':
                    obj_to_parse += sym
                    
2+2