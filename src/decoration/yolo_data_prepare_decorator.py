import cv2
import numpy as np
from PIL.Image import Image
from PIL.JpegImagePlugin import JpegImageFile

from src.contracts.decoration.deep_learning_prep_data_decorator import DLPrepDataDecoratorAbstract
from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class YoloDataPrepareDecorator(DLPrepDataDecoratorAbstract):

    def __convert_bytes(self, file: bytes):
        nparr = np.fromstring(file, np.uint8)
        return cv2.cvtColor(cv2.imdecode(nparr, cv2.IMREAD_UNCHANGED),
                            cv2.COLOR_BGR2RGB)

    def __convert_to_bytes(self, image):
        return cv2.imencode('.jpg', cv2.cvtColor(image, cv2.COLOR_RGB2BGR))[1].tobytes()

    def __convert_str(self, image_name: str):
        img = cv2.imread(image_name)
        return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    def __convert_pil(self, image: JpegImageFile):
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
        pass

    def reset_and_train(self, dataset):
        pass

    def __init__(self, dl_manager: DLModelManagerAbstract):
        super().__init__(dl_manager)
