from abc import abstractmethod

from src.contracts.decoration.deep_learning_decorator_base import DLDecoratorAbstract
from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLPrepDataDecoratorAbstract(DLDecoratorAbstract):

    def __init__(self, dl_manager: DLModelManagerAbstract):
        super().__init__(dl_manager)

    @abstractmethod
    def predict(self, image):
        """
        Подготавливает данные для процесса детекции объектов на картинке
        @param image: Изображение на котором будет происходить детекция.
        @return: Изображение с обведенными и классифицированными объектами
        """
        pass

    @abstractmethod
    def retrain(self, image, annotation):
        """
        Подготавливает данные для процесса дообучения модели
        @param image: Обучаемая картинка
        @param annotation: Аннотация меток объектов находящихся на картинке
        """
        pass

    @abstractmethod
    def reset_and_train(self, config_path: str, hyperparams: dict):
        """
        Подготавливает данные для процесса сброса и перебучения с нуля модели
        @param config_path: Путь к файлу с конфигом датасета
        @param hyperparams: Справочник гиперпараметров
        """
        pass

    @abstractmethod
    def train(self, config_path: str, hyperparams: dict):
        """
        Подготавливает данные для процесса обучения модели
        @param config_path: Путь к файлу с конфигом датасета
        @param hyperparams: Справочник гиперпараметров
        """
        pass
