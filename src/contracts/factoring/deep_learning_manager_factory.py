from abc import ABC, abstractmethod

from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLManagerFactory(ABC):

    @staticmethod
    @abstractmethod
    def get_data_preparator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        pass

    @staticmethod
    @abstractmethod
    def get_logging_decorator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        pass

    @staticmethod
    @abstractmethod
    def get_dl_manager() -> DLModelManagerAbstract:
        pass

    @staticmethod
    @abstractmethod
    def get_final_dl_manager() -> DLModelManagerAbstract:
        pass
