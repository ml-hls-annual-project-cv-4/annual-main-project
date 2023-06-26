from abc import abstractmethod

from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLDecoratorAbstract(DLModelManagerAbstract):

    @abstractmethod
    def predict(self, image):
        """
        Декорирует процесс детекции объектов на картинке
        @param image: Изображение на котором будет происходить детекция.
        @return: Изображение с обведенными и классифицированными объектами
        """
        pass

    @abstractmethod
    def retrain(self, image, annotation):
        """
        Декорирует процесс дообучения модели
        @param image: Обучаемая картинка
        @param annotation: Аннотация меток объектов находящихся на картинке
        """
        pass

    @abstractmethod
    def reset_and_train(self, config_path: str, hyperparams: dict):
        """
        Декорирует процесс сброса и перебучения с нуля модели
        @param config_path: Путь к файлу с конфигом датасета
        @param hyperparams: Справочник гиперпараметров
        """
        pass

    @abstractmethod
    def train(self, config_path: str, hyperparams: dict):
        """
        Декорирует процесс обучения модели
        @param config_path: Путь к файлу с конфигом датасета
        @param hyperparams: Справочник гиперпараметров
        """
        pass

    def __init__(self, dl_manager: DLModelManagerAbstract):
        self.dl_manager = dl_manager
