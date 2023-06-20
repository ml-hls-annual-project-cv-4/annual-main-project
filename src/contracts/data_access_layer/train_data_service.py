from abc import *


class AbstractTrainDataService(ABC):
    @abstractmethod
    def get_images_names(self):
        """
        Получает список названий изображений
        @return: список названий
        """
        pass

    @abstractmethod
    def get_images_data_by_image_name(self, image_name: str):
        """
        Получает информацию относящейся к изображению
        @param image_name: Имя изображения, у которого надо получить информацию
        @return: Данные об изображении
        """
        pass

    @abstractmethod
    def get_images_objects_by_image_name(self, image_name: str):
        """
        Собирает объекты (сущности) с изображения
        @param image_name: имя изображения, из которого надо извлечь объекты
        @return: Список объектов, находящиеся на изображении
        """
        pass
