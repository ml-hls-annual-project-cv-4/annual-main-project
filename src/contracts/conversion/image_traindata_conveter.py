from abc import ABC, abstractmethod


class ImageConverterAbstract(ABC):

    @abstractmethod
    def convert(self, image):
        pass

    @abstractmethod
    def convert(self, image, annotations):
        pass
