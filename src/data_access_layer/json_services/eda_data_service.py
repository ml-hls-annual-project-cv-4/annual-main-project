import pandas as pd

from src.data_access_layer.contracts.data_services.eda_data_service import AbstractEDADataService


class EDADataService(AbstractEDADataService):

    def get_scene_count(self, scene_name: str) -> int:
        return list(self.__get_attributes_records(self.__jsonTable)['scene']).count(scene_name)

    def get_weather_count(self, weather_name: str) -> int:
        return list(self.__get_attributes_records(self.__jsonTable)['weather']).count(weather_name)

    def get_time_of_day_count(self, time_of_day_name: str) -> int:
        return list(self.__get_attributes_records(self.__jsonTable)['timeofday']).count(time_of_day_name)

    @staticmethod
    def __get_attributes_records(table):
        """
        Получает атрибуты изображения
        @param table: источник датасета
        @return: атрибуты изображения
        """
        attributes = table['attributes']
        return pd.DataFrame.from_records(attributes)

    def get_times_of_day(self):
        return list(sorted(set(self.__get_attributes_records(self.__jsonTable)['timeofday'])))

    def get_scenes(self):
        return list(sorted(set(self.__get_attributes_records(self.__jsonTable)['scene'])))

    def get_weathers(self):
        return list(sorted(set(self.__get_attributes_records(self.__jsonTable)['weather'])))

    def __init__(self, json_file_name: str):
        self.__jsonFileName = json_file_name
        self.__jsonTable = pd.read_json(json_file_name)

    def get_categories(self):
        labels = self.__jsonTable['labels']

        categories_set = set()

        for rowIndex in range(0, len(labels)):
            for label in labels[rowIndex]:
                categories_set.add(label['category'])

        return list(sorted(categories_set))

    def get_category_count(self, category_name: str) -> int:
        category_count = 0

        labels = self.__jsonTable['labels']

        for rowIndex in range(0, len(labels)):
            for label in labels[rowIndex]:
                if category_name == label['category']:
                    category_count += 1

        return category_count
