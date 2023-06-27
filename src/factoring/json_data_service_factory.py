from src.contracts.data_access_layer.eda_data_service import AbstractEDADataService
from src.contracts.factoring.data_service_factory import AbstractDataServiceFactory
from src.json_services.eda_data_service import EDADataService


class DataServiceFactory(AbstractDataServiceFactory):

    @staticmethod
    def get_eda_data_service() -> AbstractEDADataService:
        pass

    @staticmethod
    def get_eda_data_service(json_file_name: str) -> AbstractEDADataService:
        return EDADataService(json_file_name)
