import pandas as pd

from src.Contracts.DataServices.EDADataSvc import AbstractEDADataService


class EDADataService(AbstractEDADataService):

    def GetSceneCount(self, sceneName: str) -> int:
        return list(self.__GetAttributesRecords(self.__jsonTable)['scene']).count(sceneName)

    def GetWeatherCount(self, weatherName: str) -> int:
        return list(self.__GetAttributesRecords(self.__jsonTable)['weather']).count(weatherName)

    def GetTimeOfDayCount(self, timeOfDayName: str) -> int:
        return list(self.__GetAttributesRecords(self.__jsonTable)['timeofday']).count(timeOfDayName)

    def __GetAttributesRecords(self, table):
        attributes = table['attributes']
        return pd.DataFrame.from_records(attributes)

    def GetTimesOfDay(self):
        return list(sorted(set(self.__GetAttributesRecords(self.__jsonTable)['timeofday'])))

    def GetScenes(self):
        return list(sorted(set(self.__GetAttributesRecords(self.__jsonTable)['scene'])))

    def GetWeathers(self):
        return list(sorted(set(self.__GetAttributesRecords(self.__jsonTable)['weather'])))

    def __init__(self, jsonFileName: str):
        self.__jsonFileName = jsonFileName
        self.__jsonTable = pd.read_json(jsonFileName)

    def GetCategories(self):
        labels = self.__jsonTable['labels']

        categoriesSet = set()

        for rowIndex in range(0, len(labels)):
            for label in labels[rowIndex]:
                categoriesSet.add(label['category'])

        return list(sorted(categoriesSet))

    def GetCategoryCount(self, categoryName: str) -> int:
        categoryCount = 0

        labels = self.__jsonTable['labels']

        for rowIndex in range(0, len(labels)):
            for label in labels[rowIndex]:
                if categoryName == label['category']:
                    categoryCount += 1

        return categoryCount
