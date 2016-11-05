# "dy" stands for "D"onload "Y"utube video.

import os
import tempfile

from pytube import YouTube
from pprint import pprint as pp
from slugify import slugify
from winreg import *


yt = YouTube("https://youtu.be/39IbNJzsmpM")

# pp(yt.get_videos())

mp4_videos = yt.filter('mp4')
# pp(mp4_videos)

highest_resolution_video = mp4_videos[-1]
pp("highest_resolution_video: {0}".format(highest_resolution_video))


filename = slugify(yt.filename)
pp("Renamed from {0} to {1}".format(yt.filename, filename))

yt.set_filename(filename)

# https://www.reddit.com/r/learnpython/comments/4dfh1i/how_to_get_the_downloads_folder_path_on_windows/d1r9pp1/
with OpenKey(HKEY_CURRENT_USER, 'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders') as key:
        download_directory = QueryValueEx(key, '{374DE290-123F-4565-9164-39C4925E467B}')[0]

pp(download_directory)

video = yt.get('mp4', '720p')
video.download(download_directory)



