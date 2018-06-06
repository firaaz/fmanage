#!/usr/bin/python

import argparse
import os

file_types = dict()
home = '/mnt/DATA/'
files = ['Documents', 'Music', 'Pictures', 'Torrents', 'Downloads', 'Video']
# home = os.environ['HOME']
dirc = home + 'home'

# File type bindings
file_types['Video'] = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4', 'm4v']
file_types['Music'] = ['mp3', 'mpa', 'aac', 'oga', 'ape', 'm4a', 'flac', 'm4p', 'wav']
file_types['Pictures'] = ['jpeg', 'jfif', 'exif', 'gif', 'bmp', 'png']
file_types['Documents'] = []
file_types['Movies'] = []


os.chdir(home)
if 'home' not in os.listdir(home):
    os.system('mkdir home')
os.chdir(dirc)

# creating the required files if it isnt already created
for file_name in files:
    if file_name not in os.listdir(os.getcwd()):
        os.makedirs(file_name)

for name, subdir, filename in os.walk(os.getcwd(), topdown=False):
    print(filename)
