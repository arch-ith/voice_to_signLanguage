import speech_recognition as sr
import ytdownload,test01

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        ytdownload.downloader(format(text))
        test01.generateclip(format(text))
    except:
        print("Sorry could not recognize what you said")