import os

from PIL import Image

from src.deep_learning.yolo_model_manager import YoloModelManager


def get_images():
    files = os.listdir('images')
    for file in files:
        if not (file.endswith(".jpg")):
            files.remove(file)

    return files


def test_detect_objects_in_one_image_without_errors():
    manager = YoloModelManager("models/detection_model.onnx")

    image = Image.open(os.path.join("images", get_images()[0]))

    manager.predict(image)


def test_detect_objects_in_many_images_without_errors():
    manager = YoloModelManager("models/detection_model.onnx")

    images = [Image.open(os.path.join("images", img)) for img in get_images()]

    results = [manager.predict(img) for img in images]

    assert len(images) == len(results)
