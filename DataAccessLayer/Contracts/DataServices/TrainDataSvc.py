from abc import *
import pandas as pd

class AbstractTrainDataService(ABC):
    def GetImagesNames(self):
        pass
    def GetImagesDataByImageName(self, imageName : str):
        pass
    def GetImagesObjectsByImageName(self, imageName : str):
        pass
