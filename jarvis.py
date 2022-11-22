import random
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  # this is the engine voice command
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # set the voices[0].id to get the male voice


def speak(audio):  # speak function by which the assistant speaks
    engine.say(audio)
    engine.runAndWait()


def wishMe():  # this function wish you
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning sir !")

    elif 12 <= hour < 18:
        speak("Good Afternoon sir !")

    else:
        speak("Good Evening sir !")

    speak("Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):  # this function helps us to send the mail
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        # the commands are in ifs which you said to the assistant
        # you can say anything to it but there is a defined word present in the sentence
        # for example : ok assistant, search salman khan on wikipedia.
        # mentioning wikipedia is important to catch the code

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening Youtube......')
            open("youtube.com")

        elif 'open google' in query:
            speak('Opening Google....')
            open("google.com")

        elif 'open stackoverflow' in query:
            speak('opening Stack Overflow.....')
            open("stackoverflow.com")

        elif 'play music' in query:
            speak('Playing Music....')
            music_dir = 'C:\\Users\\User\\Music\\Music'  # apni music directory daal lio
            songs = os.listdir(music_dir)
            print(songs)
            n = random.randint(0, 335)
            os.startfile(os.path.join(music_dir, songs[n]))  # song choose kr skti hai yha se ya fir random library se
            # random value bhi select kr skti hai

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak('Opening VS Code.....')
            codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  # apna path daal lio
            os.startfile(codePath)

        elif 'open microsoft edge' in query:
            speak('Opening Microsoft Edge....')
            edgePath = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"  # apna path daal lio
            os.startfile(edgePath)

        # tu kuch bhi bulva skti hai isse just ek keyword set krke
        elif 'hello' in query:
            speak("hii shruti kaushik, my boss used to say you tuti and he love you so so sooooooo much..")

        elif 'your name' in query:
            speak("I am olivia, A virtual assistant of yours..")

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "jiskoBhejnaHai@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry boss. I am not able to send this email")

        elif 'so jao' in query:
            speak("okay sir, Thank you !!! ")  # to close it just say anything with sleep
            break
