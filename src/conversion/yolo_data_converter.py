from src.contracts.conversion.image_traindata_conveter import ImageConverterAbstract
from src.contracts.dto.dataset_dto import DatasetDTO


class YoloDataConverter(ImageConverterAbstract):
    """
    Конвертер датасета для работы с моделью YOLO
    """

    def convert_data(self, image, annotations) -> DatasetDTO:
        """
        Конвертирует картинку и аннотации в пригодный вид для взаимодействия с моделью DL
        @param image: Конвертируемая картинка
        @param annotations: Конвертируемые метки объектов на изображении
        @return: Конвертированная картинка и метка. Метка должна прийти к виду class_id x_center y_center width/2 height/2. При этом сама картинка, все координаты и размеры меток нормализованы от 0 до 1.
        """
        image_size = image.size

        normalized_annotations = []

        for bbox in annotations:
            ann_temp = []

            ann_temp.append(bbox["class_id"])
            ann_temp.append((bbox["x_min"] + bbox["x_max"]) / (2 * image_size[0]))
            ann_temp.append((bbox["y_min"] + bbox["y_max"]) / (2 * image_size[1]))
            ann_temp.append((bbox["x_max"] - bbox["x_min"]) / image_size[0])
            ann_temp.append((bbox["x_max"] - bbox["x_min"]) / image_size[1])

            normalized_annotations.append(ann_temp)

        return DatasetDTO(self.convert_image(image), normalized_annotations)

    def convert_image(self, image):
        """
        Конвертирует картинку в диапазон от 0 до 1
        """

        image_res = image.copy()
        image_res /= 255

        return image_res
