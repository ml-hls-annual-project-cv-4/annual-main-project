from abc import ABC, abstractmethod


class DLModelManagerAbstract(ABC):

    @abstractmethod
    def predict(self, image):
        pass

    @abstractmethod
    def retrain(self, image, annotation):
        pass

    @abstractmethod
    def reset_and_train(self, dataset):
        pass