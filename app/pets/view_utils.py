import numpy as np
import tensorflow as tf
import keras
from keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from keras.preprocessing import image
from keras.preprocessing.image import load_img
from scipy.spatial.distance import cosine

global model
model = MobileNetV2(weights='imagenet', input_shape=(224, 224, 3), include_top=False, pooling='avg')
global graph
graph = tf.get_default_graph()


def get_embeddings(paths, model=model):
    imgs = np.array([preprocess_input(image.img_to_array(load_img(path, target_size=(224, 224, 3))))
                     for path in paths])

    with graph.as_default():
        embs = model.predict(imgs)
    return embs


def get_distances(target_emb, source_embs, metric=cosine):
    return [metric(target_emb, source_emb) for source_emb in source_embs]


def calculate_embeddings_and_get_distances(target_img_path, source_img_paths, model=model, metric=cosine):
    target_emb = get_embeddings([target_img_path], model)[0]
    source_embs = get_embeddings(source_img_paths, model)

    return get_distances(target_emb, source_embs, metric=metric)
