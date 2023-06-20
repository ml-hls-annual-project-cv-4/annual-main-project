from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract
from src.contracts.factoring.deep_learning_manager_factory import DLManagerFactory


class YoloManagerFactory(DLManagerFactory):
    @staticmethod
    def get_dl_manager() -> DLModelManagerAbstract:
        pass

    @staticmethod
    def get_image_prep_decorator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        pass

    @staticmethod
    def get_logging_decorator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        pass

    @staticmethod
    def get_final_dl_manager() -> DLModelManagerAbstract:
        return YoloManagerFactory.get_logging_decorator(
            YoloManagerFactory.get_image_prep_decorator(YoloManagerFactory.get_dl_manager()))
