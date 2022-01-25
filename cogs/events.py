import nextcord
from nextcord.ext import commands, tasks
from datetime import datetime
from tinydb import TinyDB, Query


class events(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot



    @commands.Cog.listener()
    async def on_ready(self):
        print('Logged in as')
        print(f'Time:{datetime.now()}')
        print(self.bot.user.name)
        print(self.bot.user.id)
        print('.....')
        await self.bot.change_presence(
            status=nextcord.Status.dnd,
            activity=nextcord.Activity(
                type=nextcord.ActivityType.listening,
                name=f"Everyone in #MainesianArmy"))

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "<@!933624766810697758>":

            embed = nextcord.Embed(title="I have been summoned!!", color=nextcord.Color.random(),
                                   description=f"My prefix on this server is `>`\n Simply do `>help` to see all my commands!")
            embed.set_footer(text='I was chilling until you disturbed me :(')
            await message.channel.send(embed=embed)

        if message.content.startswith(f'>afk'):
            return

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
            print("It's a DM")

        db2 = TinyDB('databases/afk.json')
        query = Query()

        for member in message.mentions:
            if db2.search(query['afk_user'] == member.id):
                value = str(
                    list(
                        map(lambda entry: entry["reason"],
                            db2.search(query['afk_user'] == member.id)))[0])
                await message.channel.send(
                    embed=nextcord.Embed(title=f"{member.display_name} is currently afk",
                                         description=f"Afk note is: {value}",
                                         color=nextcord.Color.random()))

        member = message.author
        if db2.search(query['afk_user'] == member.id):
            await message.channel.send(embed=nextcord.Embed(
                title=f"{member.display_name} You typed a message!",
                description=f"That means you ain't afk!\nWelcome back buddy.",
                color=nextcord.Color.random()))

            query = Query()
            db2.remove(query.afk_user == member.id)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(888751969722855444)
        pos = sum(m.joined_at < member.joined_at for m in member.guild.members
                  if m.joined_at is not None)
        if member.guild.id == 869173101131337748 or member.guild.id == 819870399310594088:
            member_var = member.display_name

            embed = nextcord.Embed(
                description=f"Welcome {member_var} to **{member.guild.name}**\nYou are the {pos}th member in the server.",
                color=0xe74c3c)
            embed.set_thumbnail(url=member.avatar.url)
            if not member.bot:
                try:
                    await member.send(f'Welcome to {member.guild.name}')
                except:
                    print("Could not DM")
                if not channel:
                    pass
                else:
                    await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        guild = channel.guild
        muted_role = nextcord.utils.get(guild.roles, name="Is Muted")
        if muted_role is None:
            perms = nextcord.Permissions(speak=False,
                                         send_messages=False,
                                         read_message_history=True,
                                         read_messages=True)
            try:
                await guild.create_role(name="Is Muted",
                                        color=nextcord.Color.dark_gray(),
                                        permissions=perms)

            except:
                print("New channel made, cant sync mute perms")
            try:
                muted_role = nextcord.utils.get(guild.roles, name="Is Muted")
            except:
                print("Couldnt get role :(")
        try:
            await channel.set_permissions(muted_role,
                                          send_messages=False,
                                          speak=False)
        except:
            print("Couldnt get role :(")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = self.bot.get_channel(888751969722855444)
        if member.guild.id == 869173101131337748 or member.guild.id == 819870399310594088:
            embed = nextcord.Embed(
                description=f"{member.name} left **{member.guild.name}**",
                color=0xe74c3c)
            try:
                embed.set_thumbnail(url=member.avatar.url)
            except:
                pass
            try:
                await channel.send(embed=embed)
            except:
                print("Could not get channel")



    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        db2 = TinyDB('databases/blacklist.json')
        db2q = Query()
        db2.remove(db2q.guild_id == guild.id)
        db3 = TinyDB('databases/warnings.json')
        db3q = Query()
        db3.remove(db3q.guild_id == guild.id)


def setup(bot: commands.Bot):
    bot.add_cog(events(bot))
