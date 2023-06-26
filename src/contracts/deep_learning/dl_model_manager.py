from abc import ABC, abstractmethod


class DLModelManagerAbstract(ABC):

    @abstractmethod
    def predict(self, image):
        """
        Детектирует объекты на 1 изображении
        @param image: Изображение на котором будет происходить детекция.
        @return: Изображение с обведенными и классифицированными объектами
        """
        pass

    @abstractmethod
    def retrain(self, image, annotation):
        """
        Дообучает модель по заданной картинке и аннотации
        @param image: Обучаемая картинка
        @param annotation: Аннотация меток объектов находящихся на картинке
        """
        pass

    @abstractmethod
    def reset_and_train(self, config_path: str, hyperparams: dict):
        """
        Сбрасывает модель, заново обучает и сохраняет модель по конфигу датасета и справочника гиперпараметров
        @param config_path: Путь к файлу с конфигом датасета
        @param hyperparams: Справочник гиперпараметров
        """
        pass

    @abstractmethod
    def train(self, config_path: str, hyperparams: dict):
        """
        Обучает и сохраняет модель по конфигу датасета и справочника гиперпараметров
        @param config_path: Путь к файлу с конфигом датасета
        @param hyperparams: Справочник гиперпараметров
        """
        pass