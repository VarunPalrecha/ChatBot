import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import sys
import smtplib
from googletrans import Translator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Cipher. Please tell me how may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enter your email credentials here
    server.login('varunpalrecha36', 'Sample#123')
    server.sendmail('varunpalrecha36', to, content)
    server.close()

def translateText(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
    
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=3)
            speak('According to wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            
            if songs:
                random_song_index = random.randint(0, len(songs) - 1)
                random_song = songs[random_song_index]
                print("Playing:", random_song)
                os.startfile(os.path.join(music_dir, random_song))
            else:
                print("No songs found in the directory.")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is, {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\vrpal\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open telegram' in query:
            telegramPath = "C:\\Program Files\\WindowsApps\\TelegramMessengerLLP.TelegramDesktop_4.14.9.0_x64__t4vj0pshhgkwm\\Telegram.exe"
            os.startfile(telegramPath)
        
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whom should I send this email?")
                to = input("Enter email address: ")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. I am not able to send this email at the moment.")
        
        elif 'translate' in query:
            speak("Sure, what would you like to translate?")
            text = takeCommand()
            speak("Which language would you like to translate it into?")
            target_language = takeCommand().lower()
            translated_text = translateText(text, target_language)
            speak(f"The translated text is: {translated_text}")


        elif 'shutdown cypher' in query:
            speak("Shutting down Cipher. Goodbye!")
            sys.exit()
        

