from DataAccessLayer.Contracts.DataServices.EDADataSvc import AbstractEDADataService
from DataAccessLayer.Contracts.DataServices.TrainDataSvc import AbstractTrainDataService
from DataAccessLayer.Contracts.Factories.DataSvcFactory import AbstractDataServiceFactory
from DataAccessLayer.JsonServices.JsonEDADataSvc import EDADataService


class DataServiceFactory(AbstractDataServiceFactory):
    def GetTrainDataService(self) -> AbstractTrainDataService:
        pass

    def GetEDADataService(self, source) -> AbstractEDADataService:
        return EDADataService(source)
