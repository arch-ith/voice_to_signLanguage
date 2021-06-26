from conf import SAMPLE_INPUTS,SAMPLE_OUTPUTS
from moviepy.editor import *
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import glob, os

os.chdir(SAMPLE_INPUTS)
for file in glob.glob("*.mp4"):
    if file=="alpha.mp4":
        clip=VideoFileClip(file)
        ffmpeg_extract_subclip("num.mp4", 5,7, targetname="numbers/3.mp4")

