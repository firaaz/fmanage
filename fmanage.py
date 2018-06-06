#!/usr/bin/python

import argparse
import os

home = '/mnt/DATA/'
files = ['Documents', 'Music', 'Movies', 'Pictures', 'Torrents', 'Downloads']
# home = os.environ['HOME']
dirc = home + 'home'

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
