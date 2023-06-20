from src.contracts.conversion.image_traindata_conveter import ImageConverterAbstract
from src.contracts.dto.dataset_dto import DatasetDTO


class YoloDataConverter(ImageConverterAbstract):
    def convert(self, image, bboxes) -> DatasetDTO:
        image_size = image.size

        normalized_annotations = []

        for bbox in bboxes:
            ann_temp = []

            ann_temp.append(bbox["class_id"])
            ann_temp.append((bbox["x_min"] + bbox["x_max"]) / (2 * image_size[0]))
            ann_temp.append((bbox["y_min"] + bbox["y_max"]) / (2 * image_size[1]))
            ann_temp.append((bbox["x_max"] - bbox["x_min"]) / image_size[0])
            ann_temp.append((bbox["x_max"] - bbox["x_min"]) / image_size[1])

            normalized_annotations.append(ann_temp)

        return DatasetDTO(self.convert(image), normalized_annotations)

    def convert(self, image):
        image_res = image.copy()
        image_res /= 255

        return image_res
