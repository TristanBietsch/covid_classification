import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import layers

import matplotlib.pyplot as plt
import numpy

DIRECTORY = 'Covid19-dataset/train'
CLASS_MODE = 'catagorical'
COLOR_MODE = 'greyscale'
TARGET_SIZE = (256, 256)
BATCH_SIZE  = 32

training_data_generator = ImageDataGenerator(
    rescale=1.0/255, 
    zoom_range=0.1, 
    rotation_range= 25,
    width_shift_range=0.05, 
    height_shift_range=0.05
)

