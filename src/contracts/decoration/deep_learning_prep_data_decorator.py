from abc import abstractmethod

from src.contracts.decoration.deep_learning_decorator_base import DLDecoratorAbstract
from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLPrepDataDecoratorAbstract(DLDecoratorAbstract):

    def __init__(self, dl_manager: DLModelManagerAbstract):
        super().__init__(dl_manager)

    @abstractmethod
    def train(self, config_path: str, hyperparams: dict):
        pass

    @abstractmethod
    def predict(self, image):
        pass

    @abstractmethod
    def retrain(self, image, annotation):
        pass

    @abstractmethod
    def reset_and_train(self, dataset):
        pass
