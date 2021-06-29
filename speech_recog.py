import speech_recognition as sr
import ytdownload,test01,speech_to_isl
import sys
""""
ytdownload.downloader("call accross")
test01.generateclip("call accross")

print(sys.argv[1])
s=speech_to_isl.isl(sys.argv[1])

s=speech_to_isl.isl("I am reading a story")
"""
s=speech_to_isl.isl(sys.argv[1])
s=s.strip()
print("**********************",s,"********************")
ytdownload.downloader(s)
test01.generateclip(s)
