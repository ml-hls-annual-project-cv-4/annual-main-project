import os
from typing import List

import cv2
import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset


class DrivingDataset(Dataset):

    def __init__(self,
                 root_dir: str,
                 classes: List,
                 transforms=None):
        self.root_dir = root_dir

        files = os.listdir(root_dir)

        self.imgs = sorted([x for x in files if '.jpg' in x])
        self.labels = sorted([x for x in files if '.csv' in x])

        self.classes = classes
        self.transforms = transforms

    def __load_image(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB).astype(np.float32)

        return image

    def __extract_boxes(self, img_labels: pd.DataFrame):
        return img_labels[['x_min', 'y_min', 'x_max', 'y_max']].values.tolist()

    def __getitem__(self, idx):
        image_name = self.imgs[idx]
        label_name = self.labels[idx]

        image_path = os.path.join(self.root_dir, image_name)
        labels_path = os.path.join(self.root_dir, label_name)

        image = self.__load_image(image_path)

        image_labels = pd.read_csv(labels_path, sep=';', encoding="utf8", header=0)

        labels = torch.as_tensor(image_labels['label'].apply(self.classes.index).values.tolist(), dtype=torch.int64)
        boxes = torch.as_tensor(self.__extract_boxes(image_labels), dtype=torch.float64)

        area = (boxes[:, 3] - boxes[:, 1]) * (boxes[:, 2] - boxes[:, 0])
        iscrowd = torch.zeros((boxes.shape[0],), dtype=torch.int64)

        target = {}
        target['boxes'] = boxes
        target['labels'] = labels

        if self.transforms:
            augmented = self.transforms(image=image,
                                        bboxes=target['boxes'],
                                        labels=labels)

            image = augmented['image']
            target['boxes'] = torch.tensor(augmented['bboxes'])

        return image, target

    def __len__(self):
        return len(self.imgs)
