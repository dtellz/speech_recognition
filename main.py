from re import search
import speech_recognition as sr
import webbrowser
from time import ctime

r = sr.Recognizer()


def respond(voiceData):
    if 'what is your name' in voiceData:
        print('My name is Delta')
    if 'what time is it' in voiceData:
        print(ctime())
    if 'search' in voiceData:
        search = recordAudio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        print('This is what I found for ' + search)
    if 'find location' in voiceData:
        location = recordAudio('Where do you want to go?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        print('Enjoy the ride to ' + location)
    if 'show me a video' in voiceData:
        video = recordAudio('What do you want to watch?')
        url = 'https://www.youtube.com/results?search_query=' + video
        webbrowser.get().open(url)
        print('Just relax and watch ' + video)


def recordAudio(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        try:
            voiceData = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I did not understand you my friend!')
        except sr.RequestError:
            print('Sorry I have a problem right now and I cant listen properly :(')
        return voiceData


print("Hi, I am Diego's assistant bot, what do you need?")
voiceData = recordAudio()
respond(voiceData)
