from abc import *

from src.Contracts.DataServices.EDADataSvc import AbstractEDADataService
from src.Contracts.DataServices.TrainDataSvc import AbstractTrainDataService


class AbstractDataServiceFactory(ABC):
    @abstractmethod
    def GetEDADataService(self) -> AbstractEDADataService:
        pass

    @abstractmethod
    def GetTrainDataService(self) -> AbstractTrainDataService:
        pass