#!/usr/bin/env python3

import pyttsx3
import datetime

class SupremeVoiceAssistant:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.greet_user()

    def speak(self, text):
        print(f"🗣️ Supreme Says: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def greet_user(self):
        hour = datetime.datetime.now().hour
        if hour < 12:
            self.speak("Good morning, Supreme General.")
        elif hour < 18:
            self.speak("Good afternoon, Supreme General.")
        else:
            self.speak("Good evening, Supreme General.")

        self.speak("RDG Voice Assistant Activated.")

if __name__ == "__main__":
    assistant = SupremeVoiceAssistant()
