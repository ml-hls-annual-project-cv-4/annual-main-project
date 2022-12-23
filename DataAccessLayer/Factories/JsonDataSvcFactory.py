from src.Contracts.DataServices.EDADataSvc import AbstractEDADataService
from src.Contracts.DataServices.TrainDataSvc import AbstractTrainDataService
from src.Contracts.Factories.DataSvcFactory import AbstractDataServiceFactory
from src.JsonServices.JsonEDADataSvc import EDADataService


class DataServiceFactory(AbstractDataServiceFactory):
    def GetTrainDataService(self) -> AbstractTrainDataService:
        pass

    def GetEDADataService(self, jsonFileName: str) -> AbstractEDADataService:
        return EDADataService(jsonFileName)
