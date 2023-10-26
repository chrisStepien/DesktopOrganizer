# Python program to organize files on the desktop into folders

# importing os module
import os 

# importing shutil module
import shutil

# desktop path
path = 'C:/Users/chris/OneDrive/Desktop'

print(os.listdir(path))