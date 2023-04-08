'''
This module provides pipeline for "one-image" prediction using hog vectors.
It's supposed to be used by fastapi predict_service. 
We can pass an image local path or image parsed as a ndarray.
To make a prediction meaningful we should pass image with boxes coordinates or precutted image.

Pipeline #1: Pass any image and two point coordinates. 
These coordinates will be considered as rectangle's diagonal points and used for cutting a box.
This box will be the final image we are gonna work with.
----------------------------------------
HogPredict(img_path='11219096-d4840255.jpg') \
    .cut_box(x1, y1, x2, y2) \
    .convert_to_hog() \
    .make_pred()
----------------------------------------

Pipeline #2: Pass a prepared image. The object you want to classify must take the whole image area.
It can be any image but be sure it will be recognized as a car no matter what it is.
Instead of passing img_path we can provide np.ndarray corresponded to image.
----------------------------------------
HogPredict(data=img_bgr_array) \
    .convert_to_hog() \
    .make_pred()
----------------------------------------

'''

import cv2
import numpy as np
import pickle
from skimage.feature import hog
import lightgbm

class HogPredict():
    
    def __init__(self, data=None, img_path=None):
        if data is None and img_path is None:
            raise ValueError('You should provide at least one argument ether data or img_path')
        
        if data is not None:
            self.data = data
        else:
            self.img_path = img_path
            self.data = cv2.imread(self.img_path)
        
    def cut_box(self, x1, y1, x2, y2):
        '''
        Function cuts box from image array by two points coordinates.
        Coordinates can be float or integer.
        '''
        
        self.data = self.data[int(np.floor(y1)):int(np.ceil(y2)), int(np.floor(x1)):int(np.ceil(x2))]
        
        return self
            
    def convert_to_hog(self):
        '''
        To use hog vectors in any model we need them to be the same length.
        To reach that goal we're standartizing all images to one shape (width/height rate).
        After that func converts image 2d array to hog vector
        '''
            
        width = self.data.shape[1]
        height = self.data.shape[0]
        
        if min(width, height) < 32:
            size = 32
        else :
            size = int(32*2**np.floor(np.log2(min(width, height) // 32)))
            
        image_resized = cv2.resize(self.data, (size, size))
        self.data = hog(image_resized, orientations=8, pixels_per_cell=(int(size / 8), int(size / 8)), 
                        cells_per_block=(2,2), channel_axis = -1, visualize=False)
        
        return self
        
    def make_pred(self, model_path='src/features_extraction_algorithms/best_hog_estimator_short.pickle'):
        '''
        Function makes prediction for one hog vector. The shape must be (1, 1568). 
        If a simple array were passed it's gonna be converted to consistent format
        It can be a ndarray or a DataFrame. 
        We are using precalculated lightgbm model for prediction
        '''
        
        with open(model_path, 'rb') as file:
            pckl_model = pickle.load(file)
                
        if self.data.shape != (1,1568):
            array_for_pred = np.ndarray(shape=(1,1568))
            array_for_pred[0, :] = self.data
        else:
            array_for_pred = self.data
        
        return pckl_model.predict(array_for_pred)[0]
    
    pass
