import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')

@bot.command()
async def dodaj(ctx, a: int, b: int):
    await ctx.send(f'Suma: {a + b}')

@bot.command()
async def odejmij(ctx, a: int, b=10):
    await ctx.send(f'Różnica {a - b}')

@bot.command()
async def pomnoz(ctx, a: int, b: int):
    await ctx.send(f'Wynik: {a * b}')

@bot.command()
async def podziel(ctx, a: int, b: int):
    await ctx.send(f'Wynik: {a / b}')

@bot.command()
async def hej(ctx, count=5):
    await ctx.send('Hej!' * 5)

import random
@bot.command()
async def haslo(ctx, dlugosc: int):
    symbols = 'ABCDEFGHIJKLMNOUPRSTWYZXabcdefghijklmnouprstwyzx01234567890!@#'
    password = ''
    for i in range(dlugosc):
        password += random.choice(symbols)
    await ctx.send(f'Twoje hasło to {password}')

@bot.command()
async def repeat(ctx, times: int, content='Powtórz'):
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def flip_coin(ctx):
    coin = random.choice(['orzeł', 'resztka'])
    await ctx.send(f'Rzut monetą... {coin}')

choices = ['kamień', 'papier','nożyce']
@bot.command()
async def rps(ctx, choice):
    user_choice = choice.lower()
    if user_choice not in choices:
        await ctx.send('Niepoprawny wybór!')
        return
    bot_choice = random.choice(choices)
    if user_choice == bot_choice:
        await ctx.send(f'Rezultat: Remis! Wybrałem {bot_choice}')
        return
    elif (user_choice == 'kamień' and bot_choice == 'nożyce') or \
         (user_choice == 'papier' and bot_choice == 'kamień') or \
         (user_choice == 'nożyce' and bot_choice == 'papier'):
        await ctx.send(f'Rezultat: Wygrałeś! Wybrałem {bot_choice}')
    else:
        await ctx.send(f'Rezultat: Przegraleś! Wybrałem {bot_choice}')

bot.run(token)
