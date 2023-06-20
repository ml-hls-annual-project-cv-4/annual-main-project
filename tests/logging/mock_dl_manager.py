from src.contracts.deep_learning.dl_model_manager import DLModelManagerAbstract


class MockDLManager(DLModelManagerAbstract):
    def predict(self, image):
        print("Mock Predict")

    def retrain(self, image, annotation):
        print("Mock Retrain")

    def reset_and_train(self, dataset):
        print("Mock Reset And Train")