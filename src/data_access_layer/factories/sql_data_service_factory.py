from src.data_access_layer.contracts.data_services.eda_data_service import AbstractEDADataService
from src.data_access_layer.contracts.data_services.train_data_service import AbstractTrainDataService
from src.data_access_layer.contracts.factories.data_service_factory import AbstractDataServiceFactory
from src.data_access_layer.sql_services.train_data_service import TrainDataService


class DataServiceFactory(AbstractDataServiceFactory):
    @staticmethod
    def get_train_data_service(source) -> AbstractTrainDataService:
        return TrainDataService(source)

    @staticmethod
    def get_eda_data_service(self, source) -> AbstractEDADataService:
        pass
