#!/usr/bin/python

import argparse
import os

home = '/mnt/DATA/'
os.chdir(home)
os.system('mkdir home')
dirc = home + 'home'
os.chdir(dirc)
os.system('mkdir ' + ' '.join(['Documents', 'Music', 'Movies', 'Pictures', 'Torrents']))
# for x in os.listdir(home):
#    if 'Downloads' == x:
#        dirc = home + 'Downloads'
#        os.chdir(dirc)
#
#        print(os.getcwd())
#        print(os.listdir())
