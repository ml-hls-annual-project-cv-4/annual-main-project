from abc import *


class AbstractEDADataService(ABC):

    @abstractmethod
    def GetCategories(self):
        pass

    @abstractmethod
    def GetCategoryCount(self, categoryName: str) -> int:
        pass

    @abstractmethod
    def GetSceneCount(self, sceneName: str) -> int:
        pass

    @abstractmethod
    def GetWeatherCount(self, weatherName: str) -> int:
        pass

    @abstractmethod
    def GetTimeOfDayCount(self, timeOfDayName: str) -> int:
        pass

    @abstractmethod
    def GetScenes(self):
        pass

    @abstractmethod
    def GetWeathers(self):
        pass

    @abstractmethod
    def GetTimesOfDay(self):
        pass
