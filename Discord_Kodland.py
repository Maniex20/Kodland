import discord
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Zalogowano jako {client.user}')


import random
def gen_pass(pass_len):
    elements = 'abcdefghijklmnouprstwyxzABCDEFGHIJKLMNOUPRSTWYZ0123456789'
    password = ''
    for i in range(pass_len):
        password += random.choice(elements)
    return password

def flip_coin():
    choice = ['orzeł', 'resztka']
    return random.choice(choice)

def random_emotki():
    e = [':smile:', ':heart:', ':wink:']
    return random.choice(e)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('!smile'):
        await message.channel.send(':sunglasses:')
    elif message.content.startswith('!password'):
        await message.channel.send('Twoje hasło to: ' + gen_pass(10))
    elif message.content.startswith('!coin'):
        await message.channel.send('Wypadło: ' + flip_coin())
    elif message.content.startswith('!emotki'):
        await message.channel.send('Wylosowano: ' + random_emotki())

client.run('')
