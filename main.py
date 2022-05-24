import discord
import logging
import requests
from bs4 import BeautifulSoup

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "OTc4NjUzODc2MjA0OTk4NjU2.Gn0rKL.4PGBNDbWYHiOrm6tnHzMwYyVbvX7W-_Cb9d9UY" # вставь свой токен


class YLBotClient(discord.Client):
    async def on_ready(self):
        logger.info(f'{self.user} has connected to Discord!')
        for guild in self.guilds:
            logger.info(
                f'{self.user} подключились к чату:\n'
                f'{guild.name}(id: {guild.id})')

    async def on_message(self, message):
        if message.author == self.user:
            return
        if "кот" in message.content.lower():
            req = requests.get('https://api.thecatapi.com/v1/images/search?format=src')
            url = req.url
            await message.channel.send(url)
        else:
            await message.channel.send("Спасибо за сообщение")


intents = discord.Intents.default()
intents.members = True
client = YLBotClient(intents=intents)
client.run(TOKEN)
