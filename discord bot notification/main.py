import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime, timedelta

# Enable intents for member status tracking
intents = discord.Intents.default()
intents.members = True
intents.presences = True  # Required to track online status

bot = commands.Bot(command_prefix='!', intents=intents)


CHANNEL_ID = YOUR_CHANNEL_ID  

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.wait_until_ready()  
    hourly_notification.start()

@tasks.loop(hours=3)
async def hourly_notification():
    channel = bot.get_channel(CHANNEL_ID)
    
    if not channel:
        print("Channel not found! Make sure the bot has access.")
        return
    
    # Send reminder messages
    await channel.send("You've been online for more than 3 hours! Ride a bike or something. 🚴‍♂️")
    await asyncio.sleep(2)
    await channel.send("Or maybe...")
    await asyncio.sleep(2)
    await channel.send("Make a code or make a game if you have free time! 🤖👾🚀⏰")
    
    # Get the current UTC time
    current_time = datetime.utcnow()

    # Check all members in the guild
    for member in channel.guild.members:
        if member.status == discord.Status.online:  
            joined_at = member.joined_at or datetime.utcnow() 
            time_online = (current_time - joined_at).total_seconds()

            # If online for more than 3 hours, send a reminder
            if time_online > 10800:  # 3 hours in seconds
                await channel.send(f"{member.mention}, you've been online for more than 3 hours! Take a break. 😴")

bot.run('YOUR_BOT_TOKEN')  # Replace with your actual bot token
