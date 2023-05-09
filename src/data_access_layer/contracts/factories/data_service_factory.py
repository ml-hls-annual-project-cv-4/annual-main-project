from abc import *

from src.data_access_layer.contracts.data_services.eda_data_service import AbstractEDADataService
from src.data_access_layer.contracts.data_services.dataset_loader import AbstractionDatasetLoader


class AbstractDataServiceFactory(ABC):
    @abstractmethod
    def get_eda_data_service(self, source) -> AbstractEDADataService:
        """
        Получает сервис данных для разведочного анализа
        @return: ссылку на сервис данных разведочного анализа (под капотом абстрактный класс AbstractEDADataService)
        """
        pass

    def get_dataset_loader(self, source : dict) -> AbstractionDatasetLoader:
        """
        Получает сервис извлечения данных для их использования в обучении модели
        @param source: источник данных для сервиса
        @return:
        """
        pass
