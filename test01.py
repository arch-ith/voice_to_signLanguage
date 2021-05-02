from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
import glob, os

s = "call brother"
s= list(s.split(" "))
c=0
dic = {}
for w in s:
    dic[c]=w
    c+=1
clips = [None]*len(s)

os.chdir(SAMPLE_INPUTS)
for key, value in dic.items():
    for file in glob.glob("*.mp4"):
        if value.lower() ==os.path.splitext(file)[0].lower():
            clip = VideoFileClip(file)
            #if clip.size[1]>180:
                #clip=clip.resize(0.5)
            clips[key]=clip
            break
clip = concatenate_videoclips(clips,method='compose')
os.chdir(SAMPLE_OUTPUTS)
clip.write_videofile("out1.mp4")

#removing video clips from samples
os.chdir(SAMPLE_INPUTS)
#for file in glob.glob("*.mp4"):
#    os.remove(file)
