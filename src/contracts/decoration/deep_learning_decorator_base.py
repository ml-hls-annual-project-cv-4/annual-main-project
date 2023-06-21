from abc import abstractmethod

from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLDecoratorAbstract(DLModelManagerAbstract):
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

    def __init__(self, dl_manager: DLModelManagerAbstract):
        self.dl_manager = dl_manager
