import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import random
import subprocess
import cv2
import pyautogui
from numpy.random.mtrand import operator
from openai import audio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Atlas AI. Please tell me how can I help you?")



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-us')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


if __name__ == '__main__':
        wishMe()   #1

        while True:
            query = takeCommand().lower()
            if 'atlas' in query: #2
                print("Yes Sir...")
                speak("Yes sir...")


            elif 'who are you' in query: #3
                print("I am Atlas AI. Your personal assistant")
                speak("I am Atlas AI. Your personal assistant")
                print("I can do everything for you that my creator programmed me to do")
                speak("I can do everything for you that my creator programmed me to do")

            elif 'who created you' in query: #4
                print("I don't know their names but I created with python language")
                speak("I don't know their names but I created with python language")

            elif 'what is' in query: #5
                try:
                    speak("Searching wikipedia...")
                    query = query.replace("what is", "")
                    result = wikipedia.summary(query, sentences=2)
                    print(f"According to Wikipedia, {result}")
                    speak(result)
                except Exception as e:
                    print("No results found")
                    speak("No results found")

            elif 'who is' in query: #6
                try:
                    speak("Searching wikipedia...")
                    query = query.replace("who is", "")
                    result = wikipedia.summary(query, sentences=2)
                    print(f"According to Wikipedia, {result}")
                    speak(result)
                except Exception as e:
                    print("No results found")
                    speak("No results found")

            elif 'how can' in query: #5
                try:
                    speak("Searching wikipedia...")
                    query = query.replace("how can", "")
                    result = wikipedia.summary(query, sentences=5)
                    print(f"According to Wikipedia, {result}")
                    speak(result)
                except Exception as e:
                    print("No results found")
                    speak("No results found")

            elif 'just open google' in query: #7
                webbrowser.open("google.com")

            elif 'open google' in query: #8
                speak("Opening google... what would you like to search on google?")
                cm = takeCommand().lower()
                webbrowser.open(f"{cm}")
                result = wikipedia.summary(cm, sentences=2)
                speak(result)

            elif 'just open youtube' in query: #9
                webbrowser.open("youtube.com")

            elif'open youtube' in query: #10
                speak("Opening youtube... what would you like to watch on youtube?")
                cm = takeCommand().lower()
                webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")
                wk.playonyt(f"{cm}")

            elif 'search on youtube' in query: #11
                speak("What would you like to search on youtube?")
                cm = takeCommand().lower()
                webbrowser.open(f"https://www.youtube.com/results?search_query={cm}")


            elif 'close browser' in query: #12
                speak("Closing the browser")
                os.system("taskkill /f /im msedge.exe")

            elif 'what time is it now' in query: #13
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'what is the time' in query: #14
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is {strTime}")

            elif 'play music' in query: #15
                music_dir = 'F:\\Music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, random.choice(songs)))

            elif 'open notepad' in query: #16
                npath = "C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'close notepad' in query: #17
                os.system("taskkill /f /im notepad.exe")

            elif 'open command prompt' in query: #18
                os.system("start cmd")

            elif 'close command prompt' in query: #19
                os.system("taskkill /f /im cmd.exe")

            elif 'shut down the system' in query: #20
                os.system("shutdown /s /t 1")

            elif 'restart the system' in query: #21
                os.system("shutdown /r /t 1")
                
            elif 'sleep the system' in query: #22
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            # elif 'empty recycle bin' in query:
            #     try:
            #         result = subprocess.run(["powershell", "-Command", "rmdir /s %systemdrive%\$Recycle.bin"], capture_output=True,
            #                                 text=True,
            #                                 check=True)
            #         print("Recycle Bin cleared successfully.")
            #     except subprocess.CalledProcessError as e:
            #         print(f"Failed to clear Recycle Bin. Error: {e.output}")
            #
            #     # Check if the subprocess call requires elevated privileges:
            #     if result.returncode != 0:
            #         print("You might need to run the script as an administrator.")


            elif 'empty recycle bin' in query: #23
                # Command to clear the Recycle Bin (this is an example and may vary based on your OS and setup)
                command = 'powershell.exe -Command "Clear-RecycleBin -Force"'

                try:
                    result = subprocess.run(command, shell=True, check=True)
                    if result.returncode != 0:
                        print("Failed to clear Recycle Bin.")
                    else:
                        print("Recycle Bin cleared successfully.")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to clear Recycle Bin. Error: {e}")

            elif 'open camera' in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, frame = cap.read()
                    cv2.imshow('frame', frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
                cap.release()
                cv2.destroyAllWindows()

            elif 'go to sleep' in query:
                speak("alright then, I am switching off")
                quit()

            elif 'open facebook' in query:
                speak("opening facebook")
                webbrowser.open("facebook.com")

            elif 'open instagram' in query:
                speak("opening instagram")
                webbrowser.open("instagram.com")

            elif 'open microsoft word' in query:
                speak("opening microsoft word")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk")

            # elif 'open whatsapp' in query:
            #     speak("opening whatsapp")
            #     os.startfile("C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\WhatsApp.lnk")

            elif 'take screenshot' in query:
                speak("taking screenshot")
                img = pyautogui.screenshot()
                img.save("G:\\" + "screenshot" + ".png")
                speak("screenshot taken successfully")

            elif 'open calculator' in query:
                speak("opening calcutator")
                # calculate = takeCommand().lower()
                os.startfile("C:\\WINDOWS\\system32\\calc.exe")

            # elif 'type' in query:
            # query = query.replace("type", "")
            # pyautogui.typewrite(f"{query}")

            elif 'calculate' in query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("ready")
                    print("listning...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string = r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,

                    }[op]


                def eval_bianary_expr(op1, oper, op2):
                    op1, op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("your result is")
                speak(eval_bianary_expr(*(my_string.split())))