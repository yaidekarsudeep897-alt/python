
import datetime
import time

name=input("Welcome!, Enter yor name: ")
presentHour=datetime.datetime.now().hour
if 5 <= presentHour <= 11:
    print("Good Morning!", name)
elif 11<=presentHour<=17:
    print("Good Afternoon", name)
elif 17<= presentHour<=20:
    print("Good Evening", name)
else:
    print("Good Night", name)




print("Hello! Wlecome to Your Buddy ChatBot")
print("You can ask me basic question, Type 'bye' to exit from the bot")

#CahtBot memory Creation , dictionary of response

responses={
    "hello":"hi, welcome. How can I help you",
    "how are you":"I am very fine. Thank you",
    "who are you":"I am smart AI ChatBot",
    "motivate me":"Keep going. Every bug of you project makes you a better Developer",
    "happy":"Great to her that",
    "function":"learning in python",


}
#Method/Function to get response of chatBot

def getResponsOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
        
    return "I am not able to tell that yet. I am still in learning mode"

#Take user input
while True:
    userInput=input("Please ask your question: ")
    reply=getResponsOfBot(userInput)
    print("Bot response: ",reply)

    if "bye" in userInput.lower():
        break