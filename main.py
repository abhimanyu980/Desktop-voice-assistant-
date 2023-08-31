import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import random

chatStr = ""


def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"You: {query}\n AI:"
    response = openai.Completion.create(
        model="davinci-codex",
        prompt=chatStr,
        temperature=1,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    say(response["choices"][0]["text"])
    print(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    with open(f"OpenAI/{''.join(prompt.split('AI')[1:]).strip()}.txt", "w") as f:
        f.write(text)


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response: {prompt} \n *********\n\n"
    response = openai.Completion.create(
        model="davinci-codex",
        prompt=query,
        temperature=1,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/prompt- {random.randint(1, 22525545)}", "w") as f:
        f.write(text)


def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.8

        try:
            print("Recognizing..")
            audio = r.listen(source)
            query = r.recognize_google(audio, language="en-in")
            print(f"You: {query}")
            return query
        except sr.UnknownValueError:
            say("Sorry, I couldn't understand what you said. Please try again.")
            return ""


if __name__ == '__main__':
    print('PyCharm')
    say("Hello, How may I help you?")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["spotify", "https://www.spotify.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]}")
                webbrowser.open(site[1])

        if "play music" in query:  # app in laptop
            musicPath = "C:\\Users\\Lenovo\\AppData\\Roaming\\Spotify\\Spotify.exe"
            say("Opening spotify")
            os.startfile(musicPath)

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")

            say(f"The time is{hour} {min} hours")

        elif "Using AI".lower() in query.lower():
            ai(prompt=query)

        elif "Quit".lower() in query.lower():
            exit()
        elif "Reset Chat".lower() in query.lower():
            chatStr = ""


        else:
            print('Chating...')
            chat(query)
#newsapi,