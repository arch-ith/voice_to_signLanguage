from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
import glob, os

word="karen"
os.chdir(SAMPLE_INPUTS)
clips = [None]*len(word)
for i,l in enumerate(word):
    filename= l+".mp4"
    filepath = os.path.join("alphabets", filename)
    print(filepath)
    clip=  VideoFileClip(filepath)
    clips[i]=clip
clip = concatenate_videoclips(clips,method='compose')
os.chdir(SAMPLE_INPUTS)
filename= word+".mp4"
clip.write_videofile(filename)