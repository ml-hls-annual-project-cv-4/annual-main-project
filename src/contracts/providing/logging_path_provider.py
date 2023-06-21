from abc import ABC, abstractmethod


class LoggingPathProviderAbstract(ABC):

    @staticmethod
    @abstractmethod
    def get_path():
        pass