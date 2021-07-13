import fetchLink
from pytube import YouTube
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
import os
import glob
import re,wget
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


os.chdir(SAMPLE_INPUTS)
def downloader(word):
    flag=True
    word = list(word.split(" "))
    for w in word:
        for file in glob.glob("*.mp4"):
            if w.lower()==os.path.splitext(file)[0].lower(): 
                flag=False
                break
        if(flag):
            link=fetchLink.getLink(w)
            #print("*****************************",link,"******************************")
            if link==0:
                clips = [None]*len(w)
                for i,l in enumerate(w):
                    filename= l+".mp4"
                    filepath = os.path.join("alphabets", filename)
                    #print(filepath)
                    clip=  VideoFileClip(filepath)
                    clips[i]=clip
                clip = concatenate_videoclips(clips,method='compose')
                os.chdir(SAMPLE_INPUTS)
                filename= w+".mp4"
                clip.write_videofile(filename)

            elif re.match('^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',link):
                clip = YouTube(link)
                clip.streams.first().download()
            else:
                wget.download(link,out=SAMPLE_INPUTS)

