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

#Construct an ImageDataGenerator object:
DIRECTORY = 'Covid19-dataset/train'
CLASS_MODE = 'catagorical'
COLOR_MODE = 'greyscale'
TARGET_SIZE = (256, 256)
BATCH_SIZE  = 32

training_data_generator = ImageDataGenerator(
    rescale=1.0/255, #Randomly increase or decrease the size of the image by up to 10
    zoom_range=0.1, #Randomly rotate the image between -25,25 degrees
    rotation_range= 25, #Shift the image along its width by up to +/- 5%
    width_shift_range=0.05, #Shift the image along its width by up to +/- 5%
    height_shift_range=0.05 #Shift the image along its height by up to +/- 5%
)

validation_data_generator = ImageDataGenerator()
training_iterator = training_data_generator.flow_from_directory(DIRECTORY,class_mode='categorical',color_mode='grayscale',batch_size=BATCH_SIZE)#, subset='training')
training_iterator.next()

print("\nLoading validation data...")

validation_iterator = validation_data_generator.flow_from_directory(DIRECTORY,class_mode='categorical', color_mode='grayscale',batch_size=BATCH_SIZE)#, subset='validation')

#print(training_data_generator.__dict__)

def design_model(training_data):
    model = Sequential()
    # add input layer with grayscale image shape
    model.add(tf.keras.Input(shape=(256, 256, 1)))
    # convolutional hidden layers with relu functions
    # maxpooling layers and dropout layers as well
    model.add(layers.Conv2D(5, 5, strides=3, activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(layers.Dropout(0.1))
    model.add(layers.Conv2D(3,3, strides=1, activation='relu'))
    model.add(layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
    model.add(layers.Dropout(0.2))
    
    