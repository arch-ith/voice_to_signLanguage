import fetchLink
from pytube import YouTube
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
import os

#https://indiansignlanguage.org/search-dictionary/
#  (element name in indiansignlanguage.org)
os.chdir(SAMPLE_INPUTS)
def downloader(word):
    word = list(word.split(" "))
    for w in word:
        link=fetchLink.getLink(w)
        clip = YouTube(link)
        clip.streams.first().download()
