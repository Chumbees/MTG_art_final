import numpy as np
import cv2
import os
from tqdm import tqdm
from random import shuffle
import tensorflow as tf

from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *
from keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt


train_data = 'Dataset/Training'
test_data = 'Dataset/Test'
val_data = 'Dataset/Validation'

epochs = 100

def one_hot_label(img):
	label = img.split('.')[0]
	if label == 'carl_critchlow':
		ohl = np.array([1,0,0,0,0,0,0,0,0,0])
	elif label == 'christopher_moeller':
		ohl = np.array([0,1,0,0,0,0,0,0,0,0])
	elif label == 'greg_staples':
		ohl = np.array([0,0,1,0,0,0,0,0,0,0])
	elif label == 'heather_hudson':
		ohl = np.array([0,0,0,1,0,0,0,0,0,0])
	elif label == 'john_avon':
		ohl = np.array([0,0,0,0,1,0,0,0,0,0])
	elif label == 'kev_walker':
		ohl = np.array([0,0,0,0,0,1,0,0,0,0])
	elif label == 'mark_tedin':
		ohl = np.array([0,0,0,0,0,0,1,0,0,0])
	elif label == 'pete_venters':
		ohl = np.array([0,0,0,0,0,0,0,1,0,0])
	elif label == 'rob_alexander':
		ohl = np.array([0,0,0,0,0,0,0,0,1,0])
	elif label == 'ron_spencer':
		ohl = np.array([0,0,0,0,0,0,0,0,0,1])
	return ohl
	
def train_data_with_label():
	train_images = []
	for i in tqdm(os.listdir(train_data)):
		path = os.path.join(train_data, i)
		img = cv2.imread(path, cv2.IMREAD_COLOR)
		img = cv2.resize(img, (256, 256))
		train_images.append([np.array(img), one_hot_label(i)])
	shuffle(train_images)
	return train_images
	
def test_data_with_label():
	test_images = []
	for i in tqdm(os.listdir(test_data)):
		path = os.path.join(test_data, i)
		img = cv2.imread(path, cv2.IMREAD_COLOR)
		img = cv2.resize(img, (256, 256))
		test_images.append([np.array(img), one_hot_label(i)])
	shuffle(test_images)
	return test_images
	
def val_data_with_label():
	val_images = []
	for i in tqdm(os.listdir(val_data)):
		path = os.path.join(val_data, i)
		img = cv2.imread(path, cv2.IMREAD_COLOR)
		img = cv2.resize(img, (256, 256))
		val_images.append([np.array(img), one_hot_label(i)])
	shuffle(val_images)
	return val_images
	
training_images = train_data_with_label()
testing_images = test_data_with_label()
val_images = val_data_with_label()

tr_img_data = np.array([i[0] for i in training_images]).reshape(-1,256,256,3)
tr_lbl_data = np.array([i[1] for i in training_images])
tst_img_data = np.array([i[0] for i in testing_images]).reshape(-1,256,256,3)
tst_lbl_data = np.array([i[1] for i in testing_images])
val_img_data = np.array([i[0] for i in val_images]).reshape(-1,256,256,3)
val_lbl_data = np.array([i[1] for i in val_images])

model = Sequential()

model.add(InputLayer(input_shape=[256,256,3]))
model.add(Conv2D(filters=32,kernel_size=3,strides=1,padding='same',activation='relu'))
model.add(MaxPool2D(pool_size=5,padding='same'))

model.add(Conv2D(filters=64,kernel_size=3,strides=1,padding='same',activation='relu'))
model.add(MaxPool2D(pool_size=5,padding='same'))

model.add(Conv2D(filters=128,kernel_size=3,strides=1,padding='same',activation='relu'))
model.add(MaxPool2D(pool_size=5,padding='same'))

model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512,activation='relu'))
model.add(Dropout(rate=0.25))
model.add(Dense(10,activation='relu'))
optimizer = RMSprop(lr=.0001)

model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])


#Augmentation
datagen = ImageDataGenerator()
datagen.fit(tr_img_data)
history = model.fit_generator(
    datagen.flow(tr_img_data, tr_lbl_data, batch_size=128),
    steps_per_epoch=len(tr_img_data) / 32,
    epochs=epochs,
    validation_data=(val_img_data, val_lbl_data))

score = model.evaluate(tst_img_data,tst_lbl_data,verbose=0)

print('Test loss:', score[0])
print('Test accuracy:', score[1])
#/Augmentation


#model.fit(
#	x=tr_img_data,
#	y=tr_lbl_data,
#	epochs=500,
#	batch_size=100,
#	validation_data=(val_img_data, val_lbl_data))
model.summary()
history_dict = history.history;
plt.plot(range(epochs), history_dict['loss'], label='Loss')
plt.plot(range(epochs), history_dict['acc'], label='Accuracy')
plt.plot(range(epochs), history_dict['val_acc'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Performance')
plt.legend()
plt.show()