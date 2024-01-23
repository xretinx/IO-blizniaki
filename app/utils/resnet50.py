import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from utils.dog_breeds import class_names

model = tf.keras.models.load_model('models/resnet50-human_dog_model')

def preprocess_image(path):
    img = image.load_img(path, target_size=(224,224,))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    return tf.keras.applications.resnet50.preprocess_input(x)

def predict_class(path):
    img = preprocess_image(path)
    pred = model.predict(img)
    pred[0][0] -= 0.75 
    breeds = {}
    for idx, i in enumerate(class_names):
        breeds[i] = pred[0][idx]
    # idx = np.argmax(pred)
    print('resnet:', pred[0][idx], idx)
    return breeds