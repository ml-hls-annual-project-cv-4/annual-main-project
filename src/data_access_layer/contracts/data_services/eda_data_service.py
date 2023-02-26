from abc import *


class AbstractEDADataService(ABC):

    @abstractmethod
    def get_categories(self):
        """
        Получает список всех уникальных категорий из датасета
        @return: список всех уникальных категорий из датасета
        """
        pass

    @abstractmethod
    def get_scenes(self):
        """
        Получает список всех уникальных сцен из датасета
        @return: список всех уникальных сцен из датасета
        """
        pass

    @abstractmethod
    def get_weathers(self):
        """
        Получает список всех уникальных погод из датасета
        @return: список всех уникальных погод из датасета
        """
        pass

    @abstractmethod
    def get_times_of_day(self):
        """Получает список всех уникальных частей суток из датасета"""
        pass

    @abstractmethod
    def get_category_count(self, category_name: str) -> int:
        """
        Получает количество элементов определенной категории

        @param category_name: имя категории для проверки количества вхождений в датасете
        @return: целое число, которое является количеством вхождений введенной категории в датасете
        """
        pass

    @abstractmethod
    def get_scene_count(self, scene_name: str) -> int:
        """
        Получает количество изображений с определенной сценой

        @param scene_name: название сцены для проверки количества вхождений в датасете
        @return: целое число, которое является количеством изображений с введенным названием сцены
        """
        pass

    @abstractmethod
    def get_weather_count(self, weather_name: str) -> int:
        """
        Получает количество изображений с определенной погодой

        @param weather_name: название погоды для проверки количества вхождений в датасете
        @return: целое число, которое является количеством изображений с введенным названием погоды
        """
        pass

    @abstractmethod
    def get_time_of_day_count(self, time_of_day_name: str) -> int:
        """
        Получает количество изображений с определенным временем суток

        @param time_of_day_name: название времени суток для проверки количества вхождений в датасете
        @return: целое число, которое является количеством изображений с введенным типом времени суток
        """
        pass
