from abc import ABC, abstractmethod

from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLManagerFactory(ABC):

    @staticmethod
    @abstractmethod
    def get_data_preparator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        """
        Получает ссылку на абстракцию декоратора, который подготавливает данные перед непосредственным использованием сервиса DL
        @param dl_manager: Ссылка на абстракцию сервиса DL
        @return: Ссылку на абстракцию декоратора, который подготавливает данные перед непосредственным использованием сервиса DL
        """
        pass

    @staticmethod
    @abstractmethod
    def get_logging_decorator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        """
        Получает ссылку на абстракцию декоратора для логирования процессов работы менеджера DL
        @param dl_manager: Ссылка на абстракцию сервиса DL
        @return: Ссылку на абстракцию декоратора для логирования процессов работы менеджера DL
        """
        pass

    @staticmethod
    @abstractmethod
    def get_dl_manager() -> DLModelManagerAbstract:
        """
        Получает абстракцию непосредственно самого менеджера DL
        """
        pass

    @staticmethod
    @abstractmethod
    def get_final_dl_manager() -> DLModelManagerAbstract:
        """
        Возвращает полностью готовую абстракцию менеджера DL со всеми декораторами
        """
        pass
