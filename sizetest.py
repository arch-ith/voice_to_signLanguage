from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
import glob, os

os.chdir(SAMPLE_INPUTS)
for file in glob.glob("*.mp4"):
    print(file,VideoFileClip(file).size)