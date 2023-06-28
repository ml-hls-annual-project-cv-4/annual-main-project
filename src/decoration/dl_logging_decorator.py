import logging
import sys

from src.contracts.decoration.deep_learning_logging_decorator import DLLoggingDecoratorAbstract
from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLLManagerLoggingDecorator(DLLoggingDecoratorAbstract):
    """
    Абстрактный класс-декоратор, отвечающий за процесс логирования менеджера DL.
    Для логирования используется модуль logging.
    """

    def __init__(self, dl_manager: DLModelManagerAbstract, log_path):
        super().__init__(dl_manager)

        self.__log_path = log_path

        filehandler = logging.FileHandler(self.__log_path, 'a')
        filehandler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
        logger = logging.getLogger("dl_manager_logger")
        logger.setLevel(logging.INFO)
        logger.addHandler(filehandler)
        logger.addHandler(logging.StreamHandler(sys.stdout))

        self.__logger = logger

    def retrain(self, image, annotation):
        try:
            self.__logger.info("Retrain start")

            log = open(self.__log_path, 'a')

            old_stdout = sys.stdout
            sys.stdout = log

            self.dl_manager.retrain(image, annotation)

            log.close()

            self.__logger.info("Retrain succeeded")

            sys.stdout = old_stdout
        except Exception as ex:
            logging.exception(ex.__class__.__name__, exc_info=True)
            logging.info("Retrain failed")

    def reset_and_train(self, config_path: str, hyperparams: dict):
        try:
            self.__logger.info("Reset and train start")

            log = open(self.__log_path, 'a')

            old_stdout = sys.stdout
            sys.stdout = log

            self.dl_manager.reset_and_train(config_path, hyperparams)

            log.close()

            self.__logger.info("Reset and train succeeded")

            sys.stdout = old_stdout

        except Exception as ex:
            logging.exception(ex.__class__.__name__, exc_info=True)
            logging.info("Reset and train failed")

    def train(self, config_path: str, hyperparams: dict):
        try:
            self.__logger.info("Train start")

            log = open(self.__log_path, 'a')

            old_stdout = sys.stdout
            sys.stdout = log

            self.dl_manager.train(config_path, hyperparams)

            log.close()

            self.__logger.info("Train succeeded")

            sys.stdout = old_stdout

        except Exception as ex:
            logging.exception(ex.__class__.__name__, exc_info=True)
            logging.info("Train failed")

    def predict(self, image):

        try:
            self.__logger.info("Prediction start")

            log = open(self.__log_path, 'a')

            old_stdout = sys.stdout
            sys.stdout = log

            pred = self.dl_manager.predict(image)

            log.close()

            self.__logger.info("Prediction succeeded")

            sys.stdout = old_stdout

            return pred

        except Exception as ex:
            self.__logger.exception(ex.__class__.__name__)
            self.__logger.info("Prediction failed")