from src.features_extraction_algorithms.hog_algorithm import HogPredict
import pytest
import numpy as np

def test_init():
    with pytest.raises(ValueError):
        HogPredict()
        
    assert HogPredict(img_path='random_path').data is None
    
    hog_from_img = HogPredict(img_path='dataset/images/1127aff5-42799083.jpg')
    assert hog_from_img.img_path == 'dataset/images/1127aff5-42799083.jpg' and \
        isinstance(hog_from_img.data, np.ndarray) == True and \
        hog_from_img.data.shape.__len__() == 3 and \
        hog_from_img.data.shape[2] == 3
        
    hog_from_array = HogPredict(data=hog_from_img.data)
    with pytest.raises(AttributeError):
        hog_from_array.img_path
    assert isinstance(hog_from_array.data, np.ndarray) == True and \
        hog_from_array.data.shape.__len__() == 3 and \
        hog_from_array.data.shape[2] == 3
        
def test_cut_box():
    hog_from_img = HogPredict(img_path='dataset/images/1127aff5-42799083.jpg')
    assert hog_from_img.cut_box(0, 0, 5, 5).data.shape == (5, 5, 3)
    
def test_convert_to_hog():
    hog_from_img = HogPredict(img_path='dataset/images/1127aff5-42799083.jpg')
    assert hog_from_img.cut_box(0, 0, 5, 5).convert_to_hog().data.shape == (1568,)
    
    hog_from_img = HogPredict(img_path='dataset/images/1127aff5-42799083.jpg')
    assert hog_from_img.cut_box(0, 0, 70, 70).convert_to_hog().data.shape == (1568,)
    
def test_pred():
    hog_from_img = HogPredict(img_path='dataset/images/1127aff5-42799083.jpg')
    prediction = hog_from_img.cut_box(0, 0, 5, 5).convert_to_hog().make_pred()
    assert isinstance(prediction, str)
    
    hog_from_img = HogPredict(img_path='dataset/images/1127aff5-42799083.jpg')
    hog_from_img.convert_to_hog()
    array_for_pred = np.ndarray(shape=(1,1568))
    array_for_pred[0, :] = hog_from_img.data
    hog_from_img.data = array_for_pred
    assert isinstance(hog_from_img.make_pred(), str)