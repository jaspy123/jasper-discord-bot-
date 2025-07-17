import discord
import os

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ Jasper está online como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == 'ola jasper':
        await message.channel.send('Olá, Filipe! Estou pronto para ajudar 💡')

    elif message.content.lower().startswith('!ajuda'):
        await message.channel.send('Sou o Jasper. Posso ajudar-te com afiliados, automações e muito mais. Escreve "ola jasper" para começar.')

client.run(os.getenv("DISCORD_BOT_TOKEN"))
