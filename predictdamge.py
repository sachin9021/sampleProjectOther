# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 16:49:08 2018

@author: sacgawad
"""

from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img

# dimensions of our images
img_width, img_height = 128, 128

# Initialising the CNN
#classifier = Sequential()
#
img = load_img('D:/projects/car-damage-service/static/111.jpeg' , target_size=(128, 128)) # this is a PIL image 
x = img_to_array(img) # this is a Numpy array with shape (3, 256, 256)
x = x.reshape((1,) + x.shape)/64 # this is a Numpy array with shape (1, 3, 256, 256)

location = 'data2a'
model = load_model('Damseverity.h5')
prediction = model.predict(x)
print(prediction[0])
if prediction[0][0] <=.5:
    print("Front Part Of car")
   #return jsonify({'value': 'Car is damaged'})
else:
    print("Rear Part Of vehicle")