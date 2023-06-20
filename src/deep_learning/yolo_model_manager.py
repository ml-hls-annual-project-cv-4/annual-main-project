from ultralytics import YOLO

from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class YoloModelManager(DLModelManagerAbstract):

    def __init__(self, model_name):
        self.__model = YOLO(model_name, task='detect')

    def predict(self, images):
        pred = self.__model(images)

        return [res.plot() for res in pred]

    def retrain(self, image, annotation):
        pass

    def reset_and_train(self, dataset):
        pass
