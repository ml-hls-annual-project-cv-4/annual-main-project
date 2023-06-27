from src.decoration.dl_logging_decorator import DLLManagerLoggingDecorator
from src.providing.logging_path_provider import LoggingPathFolderProvider

from tests.logging.mock_dl_manager import MockDLManager
from os import path

def test_log_predict_without_errors():
    dec = DLLManagerLoggingDecorator(MockDLManager(), path.join(LoggingPathFolderProvider.get_path(), "test_dl_manager.log"))
    dec.predict(None)

def test_log_retrain_without_errors():
    dec = DLLManagerLoggingDecorator(MockDLManager(), path.join(LoggingPathFolderProvider.get_path(), "test_dl_manager.log"))
    dec.retrain(None, None)


def test_log_reset_and_train_without_errors():
    dec = DLLManagerLoggingDecorator(MockDLManager(), path.join(LoggingPathFolderProvider.get_path(), "test_dl_manager.log"))
    dec.reset_and_train(None, None)


def test_log_train_without_errors():
    dec = DLLManagerLoggingDecorator(MockDLManager(), path.join(LoggingPathFolderProvider.get_path(), "test_dl_manager.log"))
    dec.train(None, None)