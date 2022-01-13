from re import search
import speech_recognition as sr
import webbrowser
import wikipedia
import time
import pyttsx3
import datetime

r = sr.Recognizer()
r.energy_threshold = 300  # this is used to avoid noise


class person:
    name = ''

    def setName(self, name):
        self.name = name


class assistant:
    name = ''

    def setName(self, name):
        self.name = name


speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[7].id)
rate = speaker.getProperty('rate')
speaker.setProperty('rate', 173)

# BOT SPEAKING FUNCTION


def botSpeaks(text):
    speaker.say(text)
    speaker.runAndWait()


# ANSWERS TO USER VOICE


def respond(voiceData):

    if 'what is your name' in voiceData:
        botSpeaks('My name is' + bot.name)
    if 'what time is it' in voiceData:
        botSpeaks(datetime.datetime.now().strftime('%I:%M %p'))
    if 'search in google' in voiceData:
        search = recordAudio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        botSpeaks('This is what I found for ' + search)
        webbrowser.get().open(url)
    if 'find location' in voiceData:
        location = recordAudio('Where do you want to go?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        botSpeaks('Enjoy the ride to ' + location)
        webbrowser.get().open(url)
    if 'show me a video' in voiceData:
        video = recordAudio('What do you want to watch?')
        url = 'https://www.youtube.com/results?search_query=' + video
        botSpeaks('Just relax and enjoy your ' + video + 'videos')
        webbrowser.get().open(url)
    if 'tell me about' in voiceData:
        subject = recordAudio('What do you want to know about?')
        info = wikipedia.summary(subject, 1)
        botSpeaks(info)
    # if 'let me hear all your possible voices' in voiceData:
        # checkVoices()
    if 'exit' in voiceData:
        botSpeaks('Bye! I hope to see you soon')
        exit()


def recordAudio(ask=False):

    voiceData = ''
    with sr.Microphone() as source:
        if ask:
            botSpeaks(ask)
        audio = r.listen(source)
        try:
            voiceData = r.recognize_google(audio)
        except sr.UnknownValueError:
            print('Sorry, I did not understand you my friend!')
        except sr.RequestError:
            print('Sorry I have a problem right now and I cant listen properly :(')
        return voiceData


time.sleep(1)

user = person()
bot = assistant()
bot.name = 'Delta'
user.name = ''


while 1:
    voiceData = recordAudio()
    respond(voiceData)
