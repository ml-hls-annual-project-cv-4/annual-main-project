import cv2
import numpy as np

from DataAccessLayer.Contracts.DataServices.TrainDataSvc import AbstractTrainDataService


class TrainDataService(AbstractTrainDataService):
    __client = None

    def __init__(self, client):
        self.__client = client

    def GetImagesNames(self):
        images = self.__client.query_dataframe("select distinct name from images_train").values.tolist()
        return [item for sublist in images for item in sublist]

    def GetImagesDataByImageName(self, imageName: str):
        image_data = self.__client.query_dataframe(f"select * from images_train where name='{imageName}'")
        return cv2.cvtColor(np.array(image_data.img_bgr_row.values.tolist(), dtype=np.uint8), cv2.COLOR_BGR2RGB)

    def GetImagesObjectsByImageName(self, imageName: str):
        df_boxes = self.__client.query_dataframe(f"select * from boxes_train where name='{imageName}'")
        df_boxes = df_boxes[['category', 'box2d_x1', 'box2d_y1', 'box2d_x2', 'box2d_y2']]
        df_boxes.dropna(inplace=True)
        df_boxes.reset_index(drop=True, inplace=True)
        return df_boxes.to_dict('records')
