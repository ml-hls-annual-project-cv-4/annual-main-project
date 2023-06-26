import cv2
import numpy as np
from PIL.Image import Image
from PIL.JpegImagePlugin import JpegImageFile

from src.contracts.decoration.deep_learning_prep_data_decorator import DLPrepDataDecoratorAbstract
from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class YoloDataPrepareDecorator(DLPrepDataDecoratorAbstract):
    """
    Класс-декоратор, отвечающий за все конвертации данных перед непосредственным их использованием в модели YOLO
    """


    def __convert_bytes(self, file: bytes):
        """
        Конвертирует массив байтов картинки в np.ndarray
        """
        nparr = np.fromstring(file, np.uint8)
        return cv2.cvtColor(cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED),
                            cv2.COLOR_BGR2RGB)

    def __convert_to_bytes(self, image):
        """
        Конвертирует картинку np.ndarray в массив байтов
        """
        return cv2.imencode('.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))[1].tobytes()

    def __convert_str(self, image_name: str):
        """
        Считывает картинку по пути в np.ndarray
        """
        img = cv2.imread(image_name)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def __convert_pil(self, image: JpegImageFile):
        """
        Конвертирует цвета BGR в RGB
        """
        b, g, r = image.split()
        return Image.merge("RGB", (r, g, b))

    def predict(self, image):

        image_src_type = type(image)

        if image_src_type is bytes:
            return self.__convert_to_bytes(self.dl_manager.predict(self.__convert_bytes(image))[0])
        elif image_src_type is list and type(image[0]) is bytes:
            return [self.__convert_to_bytes(self.dl_manager.predict(self.__convert_bytes(img))[0]) for img in image]
        elif image_src_type is str:
            return self.dl_manager.predict(self.__convert_str(image_src_type))
        elif image_src_type is list and type(image[0]) is str:
            return [self.dl_manager.predict(self.__convert_str(img))[0] for img in image]
        elif image_src_type is JpegImageFile:
            return self.dl_manager.predict(self.__convert_pil(image))[0]
        elif image_src_type is list and type(image[0]) is JpegImageFile:
            return [self.dl_manager.predict(self.__convert_pil(img))[0] for img in image]
        elif image_src_type is np.ndarray:
            return self.dl_manager.predict(image)[0]
        elif image_src_type is list and type(image[0][0]) is np.ndarray:
            return [self.dl_manager.predict(img)[0] for img in image]
        else:
            raise TypeError(type(image))

    def retrain(self, image, annotation):
        self.dl_manager.retrain(image, annotation)

    def __prepare_hyperparams(self, hyperparams: dict):
        """
        Конвертирует данные гиперпараметров для их корректного использования в модели
        """
        if "imgsz" in hyperparams:
            hyperparams["imsz"] = tuple(hyperparams["imsz"])

        return hyperparams

    def reset_and_train(self, config_path: str, hyperparams: dict):
        self.dl_manager.reset_and_train(config_path, self.__prepare_hyperparams(hyperparams))

    def train(self, config_path: str, hyperparams: dict):
        self.dl_manager.train(config_path, self.__prepare_hyperparams(hyperparams))

    def __init__(self, dl_manager: DLModelManagerAbstract):
        super().__init__(dl_manager)
