from pytube import YouTube
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
import os

#https://indiansignlanguage.org/search-dictionary/
#  (element name in indiansignlanguage.org)


clip = YouTube("https://www.youtube.com/watch?v=jNqoK6dGDe4&feature=emb_imp_woyt")
os.chdir(SAMPLE_INPUTS)
clip.streams.first().download()
