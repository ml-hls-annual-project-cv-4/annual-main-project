import os.path

import cv2


# Надо также обновить данные и для меток в файле json, но позже. Это будет также отдельный класс
class ImageAugmentation:
    def __init__(self, path, image_name):
        """
        Инициализация сервиса аугментации изображения
        @param path: путь к папке с изображением
        @param image_name: имя изображения
        """
        self.path = path
        self.name = image_name
        self.image = cv2.imread(os.path.join(path, image_name))

    @staticmethod
    def rotate(image, angle=90, scale=1.0):
        """
        Вращает изображение на заданный угол
        @param image: Изменяемое изображение
        @param angle: Угол вращения. Положительный угол вращает против часовой стрелки, отрицательный - по часовой
        @param scale: Коэффициент масштабирования, который масштабирует изображение
        """
        w = image.shape[1]
        h = image.shape[0]

        M = cv2.getRotationMatrix2D((w / 2, h / 2), angle, scale)

        image = cv2.warpAffine(image, M, (w, h))
        return image

    @staticmethod
    def flip(image, vertical_flip=False, horizontal_flip=False):
        """
        Отражает изображение по определенным направлениям
        @param image: Изменяемое изображение
        @param vertical_flip: если True, то отражает по вертикали
        @param horizontal_flip: если True, то отражает по горизонтали
        """
        if horizontal_flip or vertical_flip:
            if horizontal_flip and vertical_flip:
                flip_code = -1
            else:
                flip_code = 0 if vertical_flip else 1
            image = cv2.flip(image, flipCode=flip_code)
        return image

    def augment(self, save_path):
        """
        Создает новые изображения на основе исходного и сохраняет их по заданному пути
        @param save_path: путь к папке для сохранения новых изображений
        """
        img = self.image.copy()
        img_flipped = self.flip(img, vertical_flip=True, horizontal_flip=False)
        img_rotated = self.rotate(img)
        img_gaussian = self.add_GaussianNoise(img)

        source_image_name, extension = os.path.splitext(self.name)

        cv2.imwrite(os.path.join(save_path, '%s' % str(source_image_name) + '_flipped' + extension), img_flipped)
        cv2.imwrite(os.path.join(save_path, '%s' % str(source_image_name) + '_rotated' + extension), img_rotated)
        cv2.imwrite(os.path.join(save_path, '%s' % str(source_image_name) + '_gaussian_noise' + extension),
                    img_gaussian)
