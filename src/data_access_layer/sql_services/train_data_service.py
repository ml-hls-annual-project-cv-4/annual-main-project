import cv2
import numpy as np

from src.data_access_layer.contracts.data_services.dataset_loader import AbstractionDatasetLoader


class TrainDataService(AbstractionDatasetLoader):
    __client = None

    def __init__(self, client):
        self.__client = client

    def get_images_names(self):
        images = self.__client.query_dataframe("select distinct name from images_train").values.tolist()
        return [item for sublist in images for item in sublist]

    def get_images_data_by_image_name(self, image_name: str):
        image_data = self.__client.query_dataframe(f"select * from images_train where name='{image_name}'")
        return cv2.cvtColor(np.array(image_data.img_bgr_row.values.tolist(), dtype=np.uint8), cv2.COLOR_BGR2RGB)

    def get_images_objects_by_image_name(self, image_name: str):
        df_boxes = self.__client.query_dataframe(f"select * from boxes_train where name='{image_name}'")
        df_boxes = df_boxes[['category', 'box2d_x1', 'box2d_y1', 'box2d_x2', 'box2d_y2']]
        df_boxes.dropna(inplace=True)
        df_boxes.reset_index(drop=True, inplace=True)
        return df_boxes.to_dict('records')
