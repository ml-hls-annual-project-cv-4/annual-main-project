import os

from PIL import Image

from src.deep_learning.yolo_model_manager import YoloModelManager

images_path = os.path.join("dataset", "images")
model_path = os.path.join("models", "detection_model.onnx")


def get_images():
    return [file for file in os.listdir(images_path) if file.endswith(".jpg")]


def test_detect_objects_in_one_image_without_errors():
    manager = YoloModelManager(model_path)

    image = Image.open(os.path.join(images_path, get_images()[0]))

    manager.predict(image)


def test_detect_objects_in_many_images_without_errors():
    manager = YoloModelManager(model_path)

    images = [Image.open(os.path.join(images_path, img)) for img in get_images()]

    results = [manager.predict(img) for img in images]

    assert len(images) == len(results)
