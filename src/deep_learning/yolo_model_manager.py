import wandb
from ultralytics import YOLO
from wandb.integration.yolov8 import add_callbacks as add_wandb_callbacks

from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class YoloModelManager(DLModelManagerAbstract):

    def __init__(self, model_name: str, config: dict = None):
        self.__model = YOLO(model_name, task='detect')

        if config is not None:
            wandb.login(key=config["secret-key"])
            wandb.init(project=config["project-name"])
            add_wandb_callbacks(self.__model, project=config["project-name"])

    def train(self, config_path: str, hyperparams: dict):
        self.__model.train(data=config_path, **hyperparams)
        self.__model.export(format='onnx')

    def predict(self, images):
        pred = self.__model(images)

        return [res.plot() for res in pred]

    def retrain(self, image, annotation):
        pass

    def reset_and_train(self, dataset):
        pass
