from keep_alive import keep_alive
import discord
import os
import random

keep_alive()

intents = discord.Intents.default()
intents.typing = False
intents.messages = True

client = discord.Client(intents=intents)

# Retrieve the bot token from environment variables
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Custom messages for specific keywords
custom_messages = {
    "ip": [
        """**⭐  ➤➤「 Here is the IP of StarLand」**
    IP - Java - StarLand.uk.to:37340
    IP - Bedrock - StarLand.uk.to
    Port - Bedrock - 37340
    Available For Minecraft Java And Bedrock Editon""",
    ],
    "start": [
        """**⭐  ➤➤「 To Start The Server  」**

**➥Step 1 GO TO **https://client.falixnodes.net/startserver 
**➥Step 2 WRITE DOWN This IP **event.falixsrv.me
**➥Step 3 VERIFY THE CAPTCHA**
**➥Step 4 CLICK ON "START SERVER**""""",
    ],
    "time": [
        """⭐ ➤➤「**Add Timer to Continue Playing!**」

➥ **Step 1** GO TO https://client.falixnodes.net/timer?id=1285958
➥ **Step 2** VERIFY THE CAPTCHA
➥ **Step 3**  CLICK ON "**ADD TIME**""""",
    ],
}

@client.event
async def on_ready():
    print(f"Logged in as {client.user.name}")
    await client.change_presence(activity=discord.Game('Swag Hai Apna ð'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.lower()

    # Check for keywords in the message content
    for keyword, replies in custom_messages.items():
        if keyword in content:
            reply = random.choice(replies)
            await message.channel.send(reply)
            return

client.run(DISCORD_TOKEN)
