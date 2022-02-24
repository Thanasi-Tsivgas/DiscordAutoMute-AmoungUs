#Athanasios Tsivgas - Amoung Us Auto Muter (discord library end)
import discord
import re
from datetime import datetime
import time

class MyClient(discord.Client):
    print("Logged in....") #library to client connection success

    async def on_voice_state_update(self, member, before, after):
        #set user
        tracker = 'DISCORDNAME#0000' #must put discord name and tag here

        #gets member as a string
        thing = str(member)
        #checks if member is the one we are looking for
        if(thing==tracker):
            #discord name minus the hash tag
            name = thing[:-5]
            before_string = str(before)
            after_string = str(after)

            #set server name, if no server name found set none
            try:
                before_server = ((before_string.split("'"))[1].split("'")[0])
            except:
                before_server = "none"

            after_server = "none"
            try:
                after_server = ((after_string.split("'"))[1].split("'")[0])
            except:
                after_server = "none"
            channel = client.get_channel(758878259479576668) #change chanel name for the chanel you want the users to be muted and un muted in (the number) - side note must be admin within discord for this to work
            members = channel.members
            #checks if user deffened or undeffened
            if(before.self_deaf!=after.self_deaf):
                if(after.self_deaf==True):
                    #if user is deaf it mutes everyone on the server
                    for member in members:
                        await member.edit(mute=True)
                        print("Muted Users")
                if(after.self_deaf==False):
                    #if user undeaf it un mutes everyone on the server
                    for member in members:
                        await member.edit(mute=False)
                    print("Un-Muted Users")


#=============================================================================
TOKEN = "DISCORD CLIENT TOKEN HERE" #enter client side discord token here (this is not for bots its for client side discord library interaction)
client = MyClient()
client.run(TOKEN, bot=False)
