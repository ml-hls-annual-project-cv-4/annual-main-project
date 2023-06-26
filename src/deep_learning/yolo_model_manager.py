from ultralytics import YOLO

from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class YoloModelManager(DLModelManagerAbstract):

    def train(self, config_path: str, hyperparams: dict):
        self.__model.train(data=config_path, **hyperparams)
        self.__model.export(format='onnx')

    def __init__(self, model_name):
        self.__model = YOLO(model_name, task='detect')

    def predict(self, images):
        pred = self.__model.predict(images, classes=[0, 1, 2, 3, 5, 6, 7, 9, 11])

        return [res.plot() for res in pred]

    def retrain(self, image, annotation):
        pass

    def reset_and_train(self, config_path: str, hyperparams: dict):
        self.__model = YOLO("yolov8n.yaml", task='detect')
        self.train(config_path, hyperparams)

