#!/usr/bin/python

import os
# import argparse
import eyed3
import shutil

# init
file_types = dict()
home = '/mnt/DATA/'
files = ['Documents', 'Music', 'Pictures', 'Torrents', 'Downloads', 'Video']
# home = os.environ['HOME'] dirc = home + 'home/'
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


def files_check_extension(directory, extension):
    for dirpath, dirnames, filenames in os.walk(directory):
        return (f for f in filenames if f.endswith('.'+extension))


def random_check():
    print("Push works")


def music_files(files):
    start_dir = os.getcwd()
    newdir = dirc + 'Music/'
    audiofile = eyed3.load(files)

    # init meta vars
    title = audiofile.tag.title
    artist = audiofile.tag.artist
    album = audiofile.tag.album

    print(title, artist, album)

    os.chdir(newdir)
    if (artist) not in os.listdir(newdir):
        os.makedirs(artist)

    os.chdir(newdir + artist)

    if (album) not in os.listdir(newdir+artist+'/'):
        os.makedirs(album)

    os.chdir(newdir)

    mvdir = newdir + '/' .join([artist, album, title])
    shutil.move(start_dir+files, mvdir)
    os.chdir(start_dir)


def files_move(files, filetype):
    start_dir = os.getcwd()
    shutil.move(start_dir+files, home+filetype)
    os.chdir(start_dir)


def main():
    os.chdir(home)
    if 'home' not in os.listdir(home):
        os.system('mkdir home')
    os.chdir(dirc)

    # creating the required files if it isn't already created
    for file_name in files:
        if file_name not in os.listdir(os.getcwd()):
            os.makedirs(file_name)

    # to find all the files and move to the specified folders
    for root in os.listdir(home):
        for folders in file_types:
            for extension in file_types[folders]:
                files_check_extension(root, extension)


print(__name__)
if __name__ == "__main__":
    main()
