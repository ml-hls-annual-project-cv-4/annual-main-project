from abc import *

from DataAccessLayer.Contracts.DataServices.EDADataSvc import AbstractEDADataService
from DataAccessLayer.Contracts.DataServices.TrainDataSvc import AbstractTrainDataService


class AbstractDataServiceFactory(ABC):
    @abstractmethod
    def GetEDADataService(self, source) -> AbstractEDADataService:
        pass

    @abstractmethod
    def GetTrainDataService(self, source) -> AbstractTrainDataService:
        pass