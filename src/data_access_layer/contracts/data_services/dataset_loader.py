from abc import *
import pandas as pd

class AbstractionDatasetLoader(ABC):

    @abstractmethod
    def get_labels_dataset(self) -> pd.DataFrame:
        """
        Получает DataFrame с метками объектов в изображениях.
        Схема: img_name, label, x_min, y_min, x_max, y_max
        @return: DataFrame меток объектов на изображениях
        """
        pass

    @abstractmethod
    def get_images_metadata(self) -> pd.DataFrame:
        """
        Получает DataFrame с метаданными изображения
        Схема: img_name, weather, scene, timeofday, timestamp
        @return: DataFrame с метаданными изображения
        """
        pass