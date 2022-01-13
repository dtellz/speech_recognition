# HI, I AM DELTA AND I AM A HOME ASSISTANT BOT :D

Python app that recognizes human language and answers acordingly


### Dependencies

```
pip install speechrecognition
pip install pyttsx3
pip install pyaudio
pip install wikipedia
pip install pywhatkit
pip install pyjokes
```

### Voice Commands

You can add other commands, but these are the ones that exist

- What is your name? -> Bot will tell you his name
- What time is it? -> Bot will tell you clock time
- Search in google -> Bot will open google in your browser with your query
- Find Location -> Bot will ask for the location and then open google maps showing it
- Show me a video -> Bot will open youtube with related videos
- Tell me about -> Bot will tell you about whatever you ask from wikipedia
- Play music -> Bot will play the song you require on youtube
- Tell me a joke -> Bot will tell you a joke
- Exit -> Bot will finish running.

### Apple Mac OS
Use Homebrew to install the prerequisite portaudio library, then install PyAudio using pip:

`brew install portaudio`
`pip install pyaudio`

pip will download the PyAudio source and build it for your version of Python.
You need to install the Command Line Tools for Xcode in order to build PyAudio with HomeBrew.
