import os
import webbrowser

import pyttsx3
import speech_recognition
import pyjokes
import random
import time

r =speech_recognition.Recognizer()

def SpeakText(command):
    engine=pyttsx3.init()
    rate=engine.getProperty('rate')
    engine.setProperty('rate',rate-80)
    engine.say(command)
    engine.runAndWait()

def Listen():
    with speech_recognition.Microphone() as source2:
        r.adjust_for_ambient_noise(source2,duration=1)
        SpeakText("Say something")
        audio2=r.listen(source2)
        try:
            MyText = r.recognize_google(audio2)
        except:
            SpeakText("Didn't recognize voice")
            SpeakText("Try again")
            Listen()
            return
        MyText=MyText.lower()

    if MyText == "hi" or MyText=="shut down":
        SpeakText("Shutting down computer in 5 ")
        SpeakText("4")
        SpeakText("3")
        SpeakText("2")
        SpeakText("1")
        SpeakText("Good Bye!")
        os.system('shutdown -s')

    elif MyText == "joke":
        SpeakText(pyjokes.get_joke())

    elif MyText == "youtube":
        SpeakText("Going to youtube in 3 ")
        SpeakText("2")
        SpeakText("1")
        webbrowser.open('https://www.youtube.com/')

    elif MyText == "game":
        t=["rock", "paper", "scissors"]
        player_score =0
        computer_score=0
        computer=t[random.randint(0,2)]
        SpeakText("Starting the game now.")
        player=0
        time.sleep(10)
        print(player)
        print(computer)

        if player==computer:
            SpeakText("tie")

        elif player=="rock":
            if computer=="paper":
                SpeakText("you lose!")
                computer_score += 1
            else:
                SpeakText("you win!")
                player_score += 1

        elif player == "paper":
            if computer == "scissors":
                SpeakText("You Lose!")
                computer_score += 1
            else:
                SpeakText("You win!")
                player_score += 1

        elif player == "scissors":
            if computer == "rock":
                SpeakText("You Lose!")
                computer_score += 1
            else:
                SpeakText("paper!")
                player_score += 1

        else:
            SpeakText("That is not a valid play. Check your spelling.")

        computer=t[random.randint(0,2)]

        SpeakText("Current Score")
        if computer_score<3 and player_score<3:
            if computer_score>player_score:
                SpeakText("you lose"+str(player_score)+""+str(computer_score))
            elif player_score > computer_score:
                SpeakText("you win"+str(player_score)+""+str(computer_score))
            else:
                SpeakText("tie" + str(player_score) + "" + str(computer_score))

        elif player_score>=3:
            SpeakText("Congratulations"+str(player_score)+""+ str(computer_score))
            Listen()
            return()

        else:
            SpeakText("You lost the game" + str(player_score) + "" + str(computer_score))
            Listen()
            return()
Listen()

