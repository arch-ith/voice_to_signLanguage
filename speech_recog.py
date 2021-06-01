import speech_recognition as sr
import ytdownload,test01
import sys
print(sys.argv[1])
ytdownload.downloader(format(sys.argv[1]))
test01.generateclip(format(sys.argv[1]))
