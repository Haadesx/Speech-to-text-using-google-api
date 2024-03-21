# Import the libraries
import speech_recognition as sr
import pyaudio

# Create a recognizer object
r = sr.Recognizer()

# Create a microphone object
mic = sr.Microphone()

# Capture audio from the microphone
with mic as source:
    # Adjust the noise level
    r.adjust_for_ambient_noise(source)
    # Listen for speech
    print("Speak now")
    audio = r.listen(source)
    # Stop listening
    print("Done listening")

# Recognize the speech using Google's service
try:
    # Use the default language
    text = r.recognize_google(audio)
    # Print the text
    print("You said: " + text)
except:
    # Handle errors
    print("Sorry, I could not understand you")
