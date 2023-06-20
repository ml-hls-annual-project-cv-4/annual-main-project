from src.contracts.providing.logging_path_provider import LoggingPathProviderAbstract
import os
from os import path


class LoggingPathFolderProvider(LoggingPathProviderAbstract):


    @staticmethod
    def get_path():
        log_path = path.join("..", "..", "logs")

        if path.exists(log_path):
            return log_path
        else:
            os.mkdir(log_path)
            return log_path

