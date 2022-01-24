from keep_alive import keep_alive
import asyncio
import nextcord
from nextcord.ext import commands, tasks
import os
from tinydb import TinyDB, Query
from dotenv import load_dotenv
load_dotenv()
from discord_slash import SlashCommand

intents = nextcord.Intents.all()

bot = commands.Bot(command_prefix='>',
                   intents=intents,
                   enable_debug_events=True)
slash = SlashCommand(bot, sync_commands=True)

bot.remove_command('help')

for filename in os.listdir('./cogs'): #this better work
    if filename.endswith('.py'):
        try:
            bot.load_extension(f"cogs.{filename[:-3]}")

        except commands.ExtensionError as e:
            print(f'{e.__class__.__name__}: {e}')


@bot.event
async def on_message(message):
    db = TinyDB('databases/blacklist.json')
    member = message.author.id
    try:
        query = Query()
        blacklisted_guild = db.search(query['guild_id'] == message.guild.id)
        blacklisted_peeps = None
        for i in range(0, len(blacklisted_guild)):
            if str(member) in str(blacklisted_guild[i]):
                blacklisted_peeps = blacklisted_guild[i]
        if blacklisted_peeps is not None:
            return

    except:
        pass

    await bot.process_commands(message=message)


@bot.command()
async def load(ctx, *, module):
    """loads a module."""
    if ctx.author.id == 815555652780294175 or ctx.author.id == 723032217504186389:
        if ctx.author.id == 815555652780294175:
            author = "Mr One"

        elif ctx.author.id == 723032217504186389:
            author = "Mr Zero"

        try:
            bot.load_extension(f"cogs.{module}")
        except commands.ExtensionError as e:
            await ctx.send(embed=nextcord.Embed(
                title=
                "Oof Buddy, there is an error <a:zo_cri:886222278331867187>",
                description=f'{e.__class__.__name__}: {e}',
                color=nextcord.Color.random()))
        else:
            embed1 = nextcord.Embed(
                title=f"Alright {author}. Loaded {module}.py with no errors",
                description=f"<a:zo_thumbs_up:886219697694081045>",
                color=nextcord.Color.random())
            await ctx.send(embed=embed1)

    else:
        await ctx.send(embed=nextcord.Embed(
            title="Nope you imposter",
            description=
            "I dont take orders from peasants like you <a:ZOWumpusTongue:865559251764903946>",
            color=nextcord.Color.random()))


@bot.command()
async def unload(ctx, *, module):
    """Unloads a module."""
    if ctx.author.id == 815555652780294175 or ctx.author.id == 723032217504186389:
        if ctx.author.id == 815555652780294175:
            author = "Mr One"

        elif ctx.author.id == 723032217504186389:
            author = "Mr Zero"

        try:
            bot.unload_extension(f"cogs.{module}")
        except commands.ExtensionError as e:
            await ctx.send(embed=nextcord.Embed(
                title=
                "Oof Buddy, there is an error <a:zo_cri:886222278331867187>",
                description=f'{e.__class__.__name__}: {e}',
                color=nextcord.Color.random()))
        else:
            embed1 = nextcord.Embed(
                title=f"Alright {author}. Unloaded {module}.py with no errors",
                description=f"<a:zo_thumbs_up:886219697694081045>",
                color=nextcord.Color.random())
            await ctx.send(embed=embed1)

    else:
        await ctx.send(embed=nextcord.Embed(
            title="Nope you imposter",
            description=
            "I dont take orders from peasants like you <a:ZOWumpusTongue:865559251764903946>",
            color=nextcord.Color.random()))


@bot.command()
async def reload(ctx, *, module):
    """reloads a module."""
    if ctx.author.id == 815555652780294175 or ctx.author.id == 723032217504186389:
        if ctx.author.id == 815555652780294175:
            author = "Mr One"

        elif ctx.author.id == 723032217504186389:
            author = "Mr Zero"

        try:
            bot.reload_extension(f"cogs.{module}")
        except commands.ExtensionError as e:
            await ctx.send(embed=nextcord.Embed(
                title=
                "Oof Buddy, there is an error<a:zo_cri:886222278331867187>",
                description=f'{e.__class__.__name__}: {e}',
                color=nextcord.Color.random()))
        else:
            embed1 = nextcord.Embed(
                title=f"Alright {author}. Reloaded {module}.py with no errors",
                description=f"<a:zo_thumbs_up:886219697694081045>",
                color=nextcord.Color.random())
            await ctx.send(embed=embed1)

    else:
        await ctx.send(embed=nextcord.Embed(
            title="Nope you imposter",
            description=
            "I dont take orders from peasants like you <a:ZOWumpusTongue:865559251764903946>",
            color=nextcord.Color.random()))


@bot.command(aliases=["reloadall", "reloadcogs"])
async def massreload(ctx):
    if ctx.author.id == 815555652780294175 or ctx.author.id == 723032217504186389:

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await ctx.send(f"Reloading {filename[:-3]}")
                await asyncio.sleep(1)
                try:
                    bot.reload_extension(f"cogs.{filename[:-3]}")
                    await ctx.send(
                        f"Done Reloading {filename[:-3]}, now moving on to the next one"
                    )

                except commands.ExtensionError as e:
                    await ctx.send(embed=nextcord.Embed(
                        title=
                        "Oof Buddy, there is an error <a:zo_cri:886222278331867187>",
                        description=f'{e.__class__.__name__}: {e}',
                        color=nextcord.Color.random()))

    else:
        await ctx.send(embed=nextcord.Embed(
            title="Nope you imposter",
            description=
            "I dont take orders from peasants like you <a:ZOWumpusTongue:865559251764903946>",
            color=nextcord.Color.random()))


@bot.command(aliases=["unloadall", "unloadcogs"])
async def massunload(ctx):
    if ctx.author.id == 815555652780294175 or ctx.author.id == 723032217504186389:
        if ctx.author.id == 815555652780294175:
            author = "Mr One"

        elif ctx.author.id == 723032217504186389:
            author = "Mr Zero"

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await ctx.send(f"Unloading {filename[:-3]}")
                await asyncio.sleep(1)
                try:
                    bot.unload_extension(f"cogs.{filename[:-3]}")
                    await ctx.send(
                        f"Done Unloading {filename[:-3]}, now moving on to the next one"
                    )

                except commands.ExtensionError as e:
                    await ctx.send(embed=nextcord.Embed(
                        title=
                        "Oof Buddy, there is an error<a:zo_cri:886222278331867187>",
                        description=f'{e.__class__.__name__}: {e}',
                        color=nextcord.Color.random()))


@bot.command(aliases=["loadall", "loadcogs"])
async def massload(ctx):
    if ctx.author.id == 815555652780294175 or ctx.author.id == 723032217504186389:
        if ctx.author.id == 815555652780294175:
            author = "Mr One"

        elif ctx.author.id == 723032217504186389:
            author = "Mr Zero"

        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await ctx.send(f"Loading {filename[:-3]}")
                await asyncio.sleep(1)
                try:
                    bot.load_extension(f"cogs.{filename[:-3]}")
                    await ctx.send(
                        f"Done Loading {filename[:-3]}, now moving on to the next one"
                    )

                except commands.ExtensionError as e:
                    await ctx.send(embed=nextcord.Embed(
                        title=
                        "Oof Buddy, there is an error <a:zo_cri:886222278331867187>",
                        description=f'{e.__class__.__name__}: {e}',
                        color=nextcord.Color.random()))

    else:
        await ctx.send(embed=nextcord.Embed(
            title="Nope you imposter",
            description=
            "I dont take orders from peasants like you <a:ZOWumpusTongue:865559251764903946>",
            color=nextcord.Color.random()))


@bot.command(aliases=["checkcogs"])
async def checkcog(ctx):
    if ctx.author.id == 815555652780294175 or ctx.author.id == 723032217504186389:
        if ctx.author.id == 815555652780294175:
            author = "Mr One"

        elif ctx.author.id == 723032217504186389:
            author = "Mr Zero"

        all_cogs = []
        loaded_cogs = []
        for filename in os.listdir('./cogs'):

            if filename.endswith('.py'):
                print(filename[:-3])
                all_cogs.append(filename[:-3])

        await ctx.send(f"Hey {author} All cogs are [{', '.join(all_cogs)}]")

        for i in all_cogs:
            try:
                bot.load_extension(f"cogs.{i}")
                await ctx.send(f"{i} wasn't loaded")
                await asyncio.sleep(1)
                bot.unload_extension(f"cogs.{i}")
            except commands.ExtensionAlreadyLoaded:
                loaded_cogs.append(i)

        await ctx.send(
            f"Hey {author} All loaded cogs are [{', '.join(loaded_cogs)}]")
    else:
        await ctx.send(embed=nextcord.Embed(
            title="Nope you imposter",
            description=
            "I dont take orders from peasants like you <a:ZOWumpusTongue:865559251764903946>",
            color=nextcord.Color.random()))


keep_alive()
token = os.getenv("token")
bot.run(token)
