from abc import ABC, abstractmethod


class ImageConverterAbstract(ABC):

    @abstractmethod
    def convert_image(self, image):
        """
        Конвертирует картинку в пригодный вид для взаимодействия с моделью DL
        @param image: Конвертируемая картинка
        """
        pass

    @abstractmethod
    def convert_data(self, image, annotations):
        """
        Конвертирует картинку и аннотации в пригодный вид для взаимодействия с моделью DL
        @param image: Конвертируемая картинка
        @param annotations: Конвертируемые метки объектов на изображении
        """
        pass
