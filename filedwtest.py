from pytube import YouTube
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
import os
import re,wget
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


os.chdir(SAMPLE_INPUTS)
link='https://www.talkinghands.co.in/sites/default/files/videos/original//Hello.mp4'
if re.match('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',link):
    clip = YouTube(link)
    clip.streams.first().download()
else:
    print("***********************************************************",link,"***************************************************************")
    #urllib.request.urlretrieve(link,SAMPLE_INPUTS)
    wget.download(link,out=SAMPLE_INPUTS)
    print("***********************************************************",link,"*222222222222222222222222222222222222222222222222222222222222")