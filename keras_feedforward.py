from __future__ import print_function

import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
import time
import os
from tensorflow.python.client import device_lib

start = time.time()
try:
    os.mkdir('result')
except Exception:
    pass
logfile = open('result/result_log.txt',"a+")

# configure the variables
batch_size = 128
num_classes = 10
epochs = 5

# double check the gpu device
print(device_lib.list_local_devices(),file=logfile)

# load the data from the build-in mnist data-set
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples',file=logfile)
print(x_test.shape[0], 'test samples',file=logfile)

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# build the feed forward model by keras
kerasmodel = Sequential()
kerasmodel.add(Dense(512, activation='relu', input_shape=(784,)))
kerasmodel.add(Dropout(0.2))
kerasmodel.add(Dense(512, activation='relu'))
kerasmodel.add(Dropout(0.2))
kerasmodel.add(Dense(10, activation='softmax'))

kerasmodel.summary()

kerasmodel.compile(loss='categorical_crossentropy',
                   optimizer=RMSprop(),
                   metrics=['accuracy'])
# train the model
history = kerasmodel.fit(x_train, y_train,
                         batch_size=batch_size,
                         epochs=epochs,
                         verbose=1,
                         validation_data=(x_test, y_test))

score = kerasmodel.evaluate(x_test, y_test, verbose=0)


print('The test loss = ', score[0],file=logfile)
print('The test accuracy = ', score[1],file=logfile)
finish = time.time()
print('The elapsed time =', finish - start ,' seconds',file=logfile)
logfile.close()