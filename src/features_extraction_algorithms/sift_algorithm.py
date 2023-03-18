import cv2
import numpy as np
from scipy.spatial.distance import cdist
from sklearn.cluster import KMeans


def extract_sift_descriptors(images):
    images_desc = []
    sift = cv2.SIFT_create()
    for image in images:
        _, desc = sift.detectAndCompute(image, None)
        images_desc.append(desc)

    return images_desc


def k_mean_bow(all_descriptors, num_cluster):
    kmeans = KMeans(n_clusters=num_cluster)
    kmeans.fit(all_descriptors)

    bow_dict = kmeans.cluster_centers_

    return bow_dict


def create_features_bow(image_descriptors, bow, num_cluster):
    X_features = []

    for i in range(len(image_descriptors)):
        features = np.array([0] * num_cluster)

        if image_descriptors[i] is not None:
            distance = cdist(image_descriptors[i], bow)

            argmin = np.argmin(distance, axis=1)

            for j in argmin:
                features[j] += 1
        X_features.append(features)

    return X_features
