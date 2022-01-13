import speech_recognition as sr

r = sr.Recognizer()


def respond(voiceData):
    if 'what is your name' in voiceData:
        print('My name is Delta')


def recordAudio():
    with sr.Microphone() as source:
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
