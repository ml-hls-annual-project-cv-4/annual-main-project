import logging
import sys

from src.contracts.decoration.deep_learning_logging_decorator import DLLoggingDecoratorAbstract
from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class DLLManagerLoggingDecorator(DLLoggingDecoratorAbstract):
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
            logging.info("Retrain failed")
            logging.exception(ex.__class__.__name__, exc_info=True)

    def reset_and_train(self, dataset):
        try:
            self.__logger.info("Reset and train start")

            log = open(self.__log_path, 'a')

            old_stdout = sys.stdout
            sys.stdout = log

            self.dl_manager.reset_and_train(dataset)

            log.close()

            self.__logger.info("Reset and train succeeded")

            sys.stdout = old_stdout

        except Exception as ex:
            logging.info("Reset and train failed")
            logging.exception(ex.__class__.__name__, exc_info=True)

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
            self.__logger.info("Prediction failed")
            self.__logger.exception(ex.__class__.__name__)
