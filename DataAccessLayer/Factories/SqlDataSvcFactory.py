from DataAccessLayer.Contracts.DataServices.EDADataSvc import AbstractEDADataService
from DataAccessLayer.Contracts.DataServices.TrainDataSvc import AbstractTrainDataService
from DataAccessLayer.Contracts.Factories.DataSvcFactory import AbstractDataServiceFactory
from DataAccessLayer.SqlServices.SqlTrainDataSvc import TrainDataService


class DataServiceFactory(AbstractDataServiceFactory):
    def GetTrainDataService(self, source) -> AbstractTrainDataService:
        return TrainDataService(source)

    def GetEDADataService(self, source) -> AbstractEDADataService:
        pass
