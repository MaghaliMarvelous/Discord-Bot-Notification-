import discord
from discord.ext import commands, tasks
import asyncio
from datetime import datetime, timedelta
import time

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    hourly_notification.start()

@tasks.loop(hours=3)
async def hourly_notification():
    channel_id = YOUR_CHANNEL_ID  # Replace with the actual channel ID where you want to send the notification
    channel = bot.get_channel(channel_id)

    if channel:
        await channel.send("You've been online for more than 3 hours!. Ride a bike or something.  https://tenor.com/view/cat-cat-watch-cat-dark-cat-light-angry-gif-21923710")
        time.sleep(2)
        await channel.send("Or maybe...")
        time.sleep(2)
        await channel.send("Make a code or make a game if you have free time! 🤖👾🚀⏰")

    if channel:
        current_time = datetime.utcnow()

        # Loop through members in the channel
        for member in channel.members:
            if member.status == discord.Status.online:
                last_message_time = member.activity.created_at if member.activity and member.activity.created_at else member.joined_at
                time_difference = current_time - last_message_time

                # Check if the member has been online for more than 2 hours
                if time_difference.total_seconds() > 10800:  # 3 hours in seconds
                    await channel.send(f"{member.mention}, you've been online for more than 2 hours! Take a break.")

bot.run('YOUR_BOT_TOKEN')  # Replace with your actual bot token
    
