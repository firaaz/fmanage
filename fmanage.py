#!/usr/bin/env python

import os
# import shutil

def initiate():
    """
    Initializations that need to be done before running the program
    input: None
    output: dict of file types
    """
    file_types = dict()
    home = './home' #for dev purpose change to "$HOME" after while completed
    files = ['Documents', 'Music', 'Pictures', 'Torrents', 'Downloads',
             'Video']

    # creating home dir if not already avaliable
    if 'home' not in os.listdir(os.getcwd()):
        os.mkdir('home')
    os.chdir(home)

    # creating the directories inside home if not already present
    for file_name in files:
        if file_name not in os.listdir(os.getcwd()):
            os.mkdir(file_name)

# File type bindings
    file_types['Video'] = [
        'webm',
        'mpg',
        'mp2',
        'mpeg',
        'mpe',
        'mpv',
        'ogg',
        'mp4',
        'm4v',
    ]
    file_types['Music'] = [
        'mp3',
        'mpa',
        'aac',
        'oga',
        'ape',
        'm4a',
        'flac',
        'm4p',
        'wav',
    ]
    file_types['Pictures'] = [
        'jpeg',
        'jfif',
        'exif',
        'gif',
        'bmp',
        'png',
    ]
    file_types['Documents'] = []

    return file_types, files

def main():
    """
    main control flow of the program
    """
    file_types = initiate()

if __name__ == '__main__':
    main()
