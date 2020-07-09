import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2


def predict(filename):
    img = cv2.imread(filename)
    img = cv2.imresize(img, (24, 24))
    model = load_model(r'C:\Users\Wojtek\Documents\Projects\DeepLearningPlayground\Resnet\model')
    img = img/255.
    prediction = model.predict(img)
    return prediction


if __name__ == '__main__':
    print(predict())
