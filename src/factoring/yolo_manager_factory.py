from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract
from src.contracts.factoring.deep_learning_manager_factory import DLManagerFactory
from src.decoration.dl_logging_decorator import DLLManagerLoggingDecorator
from src.decoration.yolo_data_prepare_decorator import YoloDataPrepareDecorator
from src.deep_learning.yolo_model_manager import YoloModelManager
from src.providing.logging_path_provider import LoggingPathFolderProvider
from os import path

class YoloManagerFactory(DLManagerFactory):
    @staticmethod
    def get_dl_manager(model_path: str) -> DLModelManagerAbstract:
        return YoloModelManager(model_path)

    @staticmethod
    def get_data_preparator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        return YoloDataPrepareDecorator(dl_manager)

    @staticmethod
    def get_logging_decorator(dl_manager: DLModelManagerAbstract) -> DLModelManagerAbstract:
        return DLLManagerLoggingDecorator(dl_manager, path.join(LoggingPathFolderProvider.get_path(), "dl_manager.log"))

    @staticmethod
    def get_final_dl_manager(model_path: str) -> DLModelManagerAbstract:
        return YoloManagerFactory.get_logging_decorator(
            YoloManagerFactory.get_data_preparator(YoloManagerFactory.get_dl_manager(model_path)))
