from pytube import YouTube
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
import os
import re,wget
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


os.chdir(SAMPLE_INPUTS)
link='https://www.youtube.com/watch?v=YgPYFmM4Sl0&ab_channel=TheSpecialGurujiOfficialTheSpecialGurujiOfficial'

if re.match('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',link):
    clip = YouTube(link)
    clip.streams.first().download()
else:
    wget.download(link,out=SAMPLE_INPUTS)