class DatasetDTO:
    """
    Класс объекта передачи данных, хранящий информацию о картинке и её меток
    """

    def __init__(self, image, annotations):
        self.Image = image
        self.Annotations = annotations
