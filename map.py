import glob, os
from moviepy.editor import *
from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS


s = "his brother become soldier"
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
            clips[key]=clip
            break
#print(clips)
