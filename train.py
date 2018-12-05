import numpy as np
import cv2
import os
from tqdm import tqdm
from random import shuffle
import tensorflow as tf

from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *

train_data = 'Dataset2/Training'
test_data = 'Dataset2/Test'
val_data = 'Dataset2/Validation'

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
		img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (360, 360))
		train_images.append([np.array(img), one_hot_label(i)])
	shuffle(train_images)
	return train_images
	
def test_data_with_label():
	test_images = []
	for i in tqdm(os.listdir(test_data)):
		path = os.path.join(test_data, i)
		img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (360, 360))
		test_images.append([np.array(img), one_hot_label(i)])
	shuffle(test_images)
	return test_images
	
def val_data_with_label():
	val_images = []
	for i in tqdm(os.listdir(val_data)):
		path = os.path.join(val_data, i)
		img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
		img = cv2.resize(img, (360, 360))
		val_images.append([np.array(img), one_hot_label(i)])
	shuffle(val_images)
	return val_images
	
training_images = train_data_with_label()
#testing_images = test_data_with_label()
val_images = val_data_with_label()

tr_img_data = np.array([i[0] for i in training_images]).reshape(-1,360,360,1)
tr_lbl_data = np.array([i[1] for i in training_images])
#tst_img_data = np.array([i[0] for i in testing_images]).reshape(-1,360,360,1)
#tst_lbl_data = np.array([i[1] for i in testing_images])
val_img_data = np.array([i[0] for i in val_images]).reshape(-1,360,360,1)
val_lbl_data = np.array([i[1] for i in val_images])

model = Sequential()

model.add(InputLayer(input_shape=[360,360,1]))
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
model.add(Dense(10,activation='softmax'))
optimizer = RMSprop(lr=.00005)

model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(
	x=tr_img_data,
	y=tr_lbl_data,
	epochs=500,
	batch_size=100,
	validation_data=(val_img_data, val_lbl_data))
model.summary()
