from src.contracts.data_access_layer.eda_data_service import AbstractEDADataService
from src.contracts.data_access_layer.train_data_service import AbstractTrainDataService
from src.contracts.factoring.data_service_factory import AbstractDataServiceFactory
from src.sql_services.train_data_service import TrainDataService


class DataServiceFactory(AbstractDataServiceFactory):
    @staticmethod
    def get_train_data_service(source) -> AbstractTrainDataService:
        return TrainDataService(source)

    @staticmethod
    def get_eda_data_service(source) -> AbstractEDADataService:
        pass
