from settings import settings
import discord
from bot_logic import gen_pass, gen_emodji, flip_coin

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('¡Hola! Soy un bot 🤖')

    elif message.content.startswith('$smile'):
        await message.channel.send(gen_emodji())

    elif message.content.startswith('$coin'):
        await message.channel.send(flip_coin())

    elif message.content.startswith('$pass'):
        await message.channel.send(gen_pass(10))

    else:
        await message.channel.send("No puedo procesar este comando 😢")

client.run(settings["TOKEN"])
