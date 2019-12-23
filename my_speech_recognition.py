import speech_recognition as sr
import webbrowser
import time
from time  import ctime

    
r=sr.Recognizer()
def record_audio(ask = False):
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=1)
        # r.energy_threshold()
        if ask:
            print(ask)
        audio= r.listen(source)
        text = ''
        try:
            text = r.recognize_google(audio)
        except:
            print("sorry, could not recognise")
        return text
def respond (text):
    if 'what is your name' in text:
        print("fatima")
    if 'what time is it' in text:
        print(ctime())
    if 'search' in text:
        search = record_audio('what do you need to search for')
        url = 'https://google.com/search?q=' +search
        webbrowser.get().open(url)
        print('hada cha l9it '+search)
    if 'location' in text:
        location = record_audio('what is the location')
        url = 'https://google.nl/maps/place/' +location+ '/&amp;'
        webbrowser.get().open(url)
        print('her is the location '+location)
    if 'exit' in text:
        exit()

time.sleep(1)
print("hello how i can help you !")
while 1:
    text = record_audio()
    respond(text)
