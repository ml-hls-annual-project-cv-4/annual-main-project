import json

import pandas as pd

from src.data_access_layer.contracts.data_services.dataset_loader import AbstractionDatasetLoader


class DatasetLoader(AbstractionDatasetLoader):

    def __init__(self, dataset_path: str):
        print('Read raw data...')
        raw_data = self.__read_raw_data(dataset_path)
        print('Reading is done')

        print('Prepare labels dataset...')
        self.__labels = self.__extract_labels_dataset(raw_data)
        print('Preparation labels is done')

        print('Prepare images metadata...')
        self.__metadata = self.__extract_metadata(raw_data)
        print('Preparation images metadata is done')

    def __read_raw_data(self, dataset_path: str) -> dict:
        with open(dataset_path, 'r') as json_file:
            return json.load(json_file)

    def __extract_labels_dataset(self, json_data: dict) -> pd.DataFrame:
        labels_dataset = []

        for json_item in json_data:
            image_name = json_item['name']

            for label in json_item['labels']:
                label_item = dict()
                label_item['image_name'] = image_name
                label_item['label'] = label['category']


                if "box2d" in label:
                    box2d = label['box2d']

                    label_item['x_min'] = box2d['x1']
                    label_item['y_min'] = box2d['y1']
                    label_item['x_max'] = box2d['x2']
                    label_item['y_max'] = box2d['y2']

                    labels_dataset.append(label_item)

        return pd.DataFrame.from_records(labels_dataset)


    def __extract_metadata(self, json_data: dict) -> pd.DataFrame:
        metadata = []

        for json_item in json_data:
            metadata_item = dict()
            metadata_item['image_name'] = json_item['name']
            metadata_item.update(json_item['attributes'])
            metadata_item['timestamp'] = json_item['timestamp']

            metadata.append(metadata_item)

        return pd.DataFrame.from_records(metadata)

    def get_images_metadata(self) -> pd.DataFrame:
        return self.__metadata

    def get_labels_dataset(self) -> pd.DataFrame:
        return self.__labels
