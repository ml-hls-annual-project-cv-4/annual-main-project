from abc import *

from src.contracts.data_access_layer.eda_data_service import AbstractEDADataService
from src.contracts.data_access_layer.train_data_service import AbstractTrainDataService


class AbstractDataServiceFactory(ABC):
    @abstractmethod
    def get_eda_data_service(self) -> AbstractEDADataService:
        """
        Получает сервис данных для разведочного анализа
        @return: ссылку на сервис данных разведочного анализа (под капотом абстрактный класс AbstractEDADataService)
        """
        pass

    def get_train_data_service(self, source) -> AbstractTrainDataService:
        """
        Получает сервис извлечения данных для их использования в обучении модели
        @param source: источник данных для сервиса
        @return:
        """
        pass
