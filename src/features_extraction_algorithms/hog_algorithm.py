'''
This module provides pipeline for "one-image" prediction using hog vectors.
It's supposed to be used by fastapi service. 
We can pass an image local path or image parsed as a ndarray.
To make a prediction meaningful we should pass image with boxes coordinates or precutted image.

Pipeline #1: The easiest way. Pass an image from the database with corresponding name. 
Then we can get boxes coordinates from database
----------------------------------------
img_bgr_array = img_to_array(img_path)
df_labels = dwh.select_db_labels(ls_names, tbl_name)
prediction = (
    df_labels[lambda df: np.invert(df.box2d_x1.isna())]
        .apply(lambda df: img_cut_box(img_bgr_array, df.box2d_x1, df.box2d_y1, df.box2d_x2, df.box2d_y2), 
               axis=1)
        .apply(convert_to_hog)
        .apply(make_pred_hog_vc)
        .apply(np.squeeze)
        .to_numpy()
)
----------------------------------------

Pipeline #2: Pass a prepared image. The object you want to classify must take the whole image area.
It can be any image but be sure it will be recognized as a car no matter what it is.
----------------------------------------
img_bgr_array = img_to_array(img_path)
hog_vc = convert_to_hog(img_bgr_array)
prediction = make_pred_hog_vc(hog_vc)
----------------------------------------

Pipeline #3: Pass any image and two point coordinates. 
These coordinates will be considered as rectangle's diagonal points and used for cutting a box.
This box will be the final image we are gonna work with.
----------------------------------------
img_bgr_array = img_to_array(img_path)
img_box = img_cut_box(img_bgr_array, x1, y1, x2, y2)
hog_vc = convert_to_hog(img_box)
prediction = make_pred_hog_vc(hog_vc)
----------------------------------------
'''

import cv2
import numpy as np
import src.databases.dwh as dwh
import pickle
from skimage.feature import hog
import lightgbm
import pandas as pd

def img_to_array(img_path):
    '''
    Function parses img from local path to numpy array in BGR scheme 
    '''
    
    return cv2.imread(img_path)

def img_cut_box(img_array, x1, y1, x2, y2):
    '''
    Function cuts box from image array by two points coordinates.
    Coordinates can be float or integer.
    '''
    
    return img_array[int(np.floor(y1)):int(np.ceil(y2)), int(np.floor(x1)):int(np.ceil(x2))]

def convert_to_hog(img_array):
    '''
    To use hog vectors in any model we need them to be the same length.
    To reach that goal we're standartizing all images to one shape (width/height rate).
    After that func converts image 2d array to hog vector
    '''
        
    width = img_array.shape[1]
    height = img_array.shape[0]
    if min(width, height) < 32:
        size = 32
    else :
        size = int(32*2**np.floor(np.log2(min(width, height) // 32)))
    img_array = cv2.resize(img_array, (size, size))    
    return hog(img_array, orientations=8, pixels_per_cell=(int(size / 8), int(size / 8)), 
               cells_per_block=(2,2), channel_axis = -1, visualize=False)

def make_pred_hog_vc(hog_vc):
    '''
    Function makes prediction for one hog vector. The shape must be (1, 1568). 
    If a simple array were passed it's gonna be converted to consistent format
    It can be a ndarray or a DataFrame. 
    We are using precalculated lightgbm model for prediction
    '''
    
    with open('src/features_extraction_algorithms/best_hog_estimator_short.pickle', 'rb') as file:
        pckl_model = pickle.load(file) 
    
    if hog_vc.shape != (1,1568):
        array_for_pred = np.ndarray(shape=(1,1568))
        array_for_pred[0, :] = hog_vc
    else:
        array_for_pred = hog_vc
    
    return pckl_model.predict(array_for_pred)
