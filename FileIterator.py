import os
from PIL import Image
import glob

y_val = [] # artist names
x_val = [] # pictures

for filename in os.listdir('Dataset2/Validation'):
	
	split_string = filename.split('.')
	artist_name = split_string[0]
	y_val.append(artist_name)
	
	im = Image.open(filename)
	x_val.append(im)
print("X_VAL")
print("Y_VAL")
