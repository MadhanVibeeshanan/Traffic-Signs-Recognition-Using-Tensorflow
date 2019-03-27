# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:27:58 2019

@author: madha
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import skimage

Root_path = "C:/Users/madha/Documents/Tensorflow Practice"

train_data_directory = os.path.join(Root_path, "Training/Training")

train_data_directory = train_data_directory.replace('\\','/')
print(train_data_directory)

def load_data(directory):
    
    directories = [d for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]
    print(directories)
    labels = []
    images = []
    for d in directories:
        label_directory = os.path.join(directory, d)
        file_names = [os.path.join(label_directory, f) for f in os.listdir(label_directory) if f .endswith(".ppm")]
    
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
        
    return images, labels
        
images, labels = load_data(train_data_directory)


