import nextcord
import asyncio
from nextcord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.utils.manage_commands import create_option, create_choice
from discord_slash.model import ButtonStyle
from discord_slash.utils.manage_components import create_button, create_actionrow
from discord_slash.utils.manage_components import wait_for_component
from discord_slash.context import ComponentContext


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(name="help",
                       description="Get help. From me of course.",
                       options=[
                           create_option(name="about",
                                         description="The thing I should help you with.",
                                         option_type=3,
                                         required=False
                                         )
                       ])
    async def _help(self, ctx: SlashContext, about=None):
        if about is None:
            page = 1
            pages = 3
            help_1 = nextcord.Embed(title="Help")
            help_1.add_field(
                name="Slowmode",
                value=f"Allows moderators to enable/disable slowmode.\n/help slowmode",
                inline=False)
            help_1.add_field(
                name="Blacklist",
                value=f"Blacklists a user.\n/help blacklist",
                inline=False)
            help_1.add_field(
                name="Unblacklist",
                value=f"Unblacklists a user.\n/help unblacklist",
                inline=False)
            help_1.add_field(
                name="Clear",
                value=f"Clears messages in a channel.\n/help clear",
                inline=False)
            help_1.add_field(
                name="Afk",
                value=f"Shows other people you are afk for some random reason.\n/help afk",
                inline=False)
            help_1.set_footer(text="Made by Frost! and Mercurius13 for Mainesia's server")
            help_1.color = nextcord.Color.random()

            help_2 = nextcord.Embed(title="Help")
            help_2.add_field(
                name="Warn",
                value=f"Gives a warning to a user. Better use coming soon!\n/help warn",
                inline=False)
            help_2.add_field(
                name="UserWarn",
                value=f"Displays the history of warnings given to a user.\n/help userwarn",
                inline=False)
            help_2.add_field(
                name="RemoveWarn",
                value=f"Removes one of, or all of, the warnings given to a user.\n/help removewarn",
                inline=False)
            help_2.add_field(
                name="Unmute",
                value=f"Unmutes a user, thus allowing then to type.\n/help unmute",
                inline=False)
            help_2.add_field(
                name="Mute",
                value=f"Stops the user from typing in the server PERMANENTLY (or until unmute).\n/help mute",
                inline=False)
            help_2.set_footer(text="Made by Frost! and Mercurius13 for Mainesia's server")
            help_2.color = nextcord.Color.random()

            help_3 = nextcord.Embed(title="Help")
            help_3.add_field(
                name="Nick",
                value=f"Change nicknames in the server by using this feature.\n/help nick",
                inline=False)
            help_3.add_field(
                name="Kick",
                value=f"Kicks the specified user from the server.\n/help kick",
                inline=False)
            help_3.add_field(
                name="Unban",
                value=f"Unbans users, obviously.\n/help unban",
                inline=False)
            help_3.add_field(
                name="Ban",
                value=f"Bans users, like, DUH.\n/help ban",
                inline=False)
            help_3.set_footer(text="Made by Frost! and Mercurius13 for Mainesia's server")
            help_3.color = nextcord.Color.random()

            buttons = [
                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                              disabled=True),
                create_button(style=ButtonStyle.blue, custom_id="back", emoji=":arrow_backward:",
                              disabled=True),
                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                              disabled=False),
                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                              disabled=False),
            ]
            action_row = create_actionrow(*buttons)

            message = await ctx.send(embed=help_1, components=[action_row])

            while True:
                try:
                    response: ComponentContext = await wait_for_component(self.bot, components=action_row,
                                                                          messages=message, timeout=300)
                    while response.author != ctx.author:
                        await response.reply("This ain't your button fool", hidden=True)
                        response: ComponentContext = await wait_for_component(self.bot, components=action_row,
                                                                              timeout=300)

                    if response.component['custom_id'] == "forward":
                        page += 1

                    elif response.component['custom_id'] == "back":
                        page -= 1

                    elif response.component['custom_id'] == "big_forward":
                        page = pages

                    elif response.component['custom_id'] == "big_back":
                        page = 1

                    if page == 1:
                        try:
                            buttons_left_disabled = [
                                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                              disabled=True),
                                create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                              disabled=True),
                                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                              disabled=False),
                            ]
                            action_row = create_actionrow(*buttons_left_disabled)
                            await response.edit_origin(embed=help_1, components=[action_row])
                        except:
                            pass

                    elif page == 2:
                        try:
                            buttons_normal = [
                                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                              disabled=False),
                            ]
                            action_row2 = create_actionrow(*buttons_normal)
                            await response.edit_origin(embed=help_2, components=[action_row2])
                        except:
                            pass

                    elif page == 3:
                        try:
                            buttons_right_disabled = [
                                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                              disabled=True),
                                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                              disabled=True),
                            ]
                            action_row3 = create_actionrow(*buttons_right_disabled)
                            await response.edit_origin(embed=help_3, components=[action_row3])
                        except:
                            pass
                    pass
                except asyncio.TimeoutError:
                    response: ComponentContext = await wait_for_component(self.bot, components=action_row,
                                                                          messages=message)
                    buttons_all_disabled = [
                        create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                      disabled=True),
                        create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                      disabled=True),
                        create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                      disabled=True),
                        create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                      disabled=True),
                    ]
                    action_row = create_actionrow(*buttons_all_disabled)
                    await response.edit_origin(components=[action_row])

        elif about.lower() == 'slowmode':
            embed = nextcord.Embed(
                title="Help Slowmode",
                description="Allows you to put or remove a slowmode in your channel.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/slowmode <timeinseconds>\nThat will stop the SPAMMERS",
                inline=True
            )
            embed.set_footer(text="Sad life for spammers.")
            await ctx.send(embed=embed)

        elif about.lower() == 'blacklist':
            embed = nextcord.Embed(
                title="Help Blacklist",
                description="This makes the required member unable to use my commands.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/blacklist @<membername>\nThis is one of the most CRUELLEST punishments possible.",
                inline=True
            )
            embed.set_footer(text="Not using CHAD be SAD")
            await ctx.send(embed=embed)

        elif about.lower() == 'unblacklist':
            embed = nextcord.Embed(
                title="Help Unblacklist",
                description="Removes blacklisted users from the list of naughty people...",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/unblacklist @<membername>\nOnly kindness can make you use this command.",
                inline=True
            )
            embed.set_footer(text="Unblacklisters = Saviours")
            await ctx.send(embed=embed)

        elif about.lower() == 'clear':
            embed = nextcord.Embed(
                title="Help Clear",
                description="Clears the required number of messages in a channel. You can also clear messages of a particular member.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/clear <numberofmessages> <optionalmember>\nHelps when your server members just don't want to stop chatting...",
                inline=True
            )
            embed.set_footer(text="Get ERASED")
            await ctx.send(embed=embed)

        elif about.lower() == 'removewarn':
            embed = nextcord.Embed(
                title="Help RemoveWarn",
                description="Used to remove one or all of a users warn.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/removewarn <reason>\nGive the reason to remove, or just type 'all' to remove all warnings.",
                inline=True)
            embed.set_footer(text="Showing mercy gets you killed. You have been warned.")
            await ctx.send(embed=embed)

        elif about.lower() == 'warn':
            embed = nextcord.Embed(title="Help Warn",
                                   description="Gives the rule-breakers a warning!",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/warn <username> <reason>\nOnly for those naughty users who don't like rules.",
                inline=True
            )
            embed.set_footer(text="So you've been warned...")
            await ctx.send(embed=embed)

        elif about.lower() == 'prefix':
            embed = nextcord.Embed(title="Help Prefix",
                                   description="Change dat prefix",
                                   color=nextcord.Color.random())
            embed.add_field(
                name="Usage:",
                value=f"/prefix <newprefix>\nVery handy for big servers!",
                inline=True
            )
            embed.set_footer(text="Just don't forget what your prefix was...")
            await ctx.send(embed=embed)

        elif about.lower() == 'userwarn':
            embed = nextcord.Embed(
                title="Help UserWarn",
                description="Gives a record of why and how many times a user was warned in the server.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/userwarn @<username>\nNow you have a record of their crimes.",
                inline=True
            )
            embed.set_footer(text="*Evil laughter from admins*")
            await ctx.send(embed=embed)

        elif about.lower() == 'unmute':
            embed = nextcord.Embed(title="Help Unmute",
                                   description="Allows you to unmute a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/unmute @<username>\nThis makes the able to talk in your server again.",
                inline=True
            )
            embed.set_footer(text="Support Freedom of Speech")
            await ctx.send(embed=embed)

        elif about.lower() == 'mute':
            embed = nextcord.Embed(title="Help Mute",
                                   description="Allows you to mute a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/mute @<username>\nNow they can't talk until you allow them too!",
                inline=True
            )
            embed.set_footer(text="Sad life for the muted")
            await ctx.send(embed=embed)

        elif about.lower() == 'kick':
            embed = nextcord.Embed(title="Help Kick",
                                   description="Allows you to kick a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/kick @<username>\nSo basically they just get yeeted out.",
                inline=True
            )
            embed.set_footer(text="Get rekt lol")
            await ctx.send(embed=embed)

        elif about.lower() == 'unban':
            embed = nextcord.Embed(title="Help Unban",
                                   description="Allows you to unban a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/unban @<username>\nSo that they can return to the server.",
                inline=True
            )
            embed.set_footer(text="Oh look, they're back lol")
            await ctx.send(embed=embed)

        elif about.lower() == 'ban':
            embed = nextcord.Embed(title="Help Ban",
                                   description="Allows you to ban a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"/ban @<username>\nThey can NEVER COME BACK NOW MWA HA HA HA\nJeez I was only joking",
                inline=True
            )
            embed.set_footer(text="Get banished lmao")
            await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(
                title="Noice",
                description=f"You ask me for help, but I can't help you\nCause {about} isn't a part of my awesome features",
                color=nextcord.Color.green())
            embed.set_footer(text=f"Try /help without anything after it")
            await ctx.send(embed=embed)

    @commands.command(aliases=['welp', 'Help'])
    async def help(self, ctx, command=None):
        if command is None:
            page = 1
            pages = 3
            help_1 = nextcord.Embed(title="Help")
            help_1.add_field(
                name="Slowmode",
                value=f"Allows moderators to enable/disable slowmode.\n{ctx.prefix}help slowmode",
                inline=False)
            help_1.add_field(
                name="Blacklist",
                value=f"Blacklists a user.\n{ctx.prefix}help blacklist",
                inline=False)
            help_1.add_field(
                name="Unblacklist",
                value=f"Unblacklists a user.\n{ctx.prefix}help unblacklist",
                inline=False)
            help_1.add_field(
                name="Clear",
                value=f"Clears messages in a channel.\n{ctx.prefix}help clear",
                inline=False)
            help_1.add_field(
                name="Afk",
                value=f"Shows other people you are afk for some random reason.\n{ctx.prefix}help afk",
                inline=False)
            help_1.set_footer(text="Made by Frost! and Mercurius13 for Mainesia's server")
            help_1.color = nextcord.Color.random()

            help_2 = nextcord.Embed(title="Help")
            help_2.add_field(
                name="Warn",
                value=f"Gives a warning to a user. Better use coming soon!\n{ctx.prefix}help warn",
                inline=False)
            help_2.add_field(
                name="UserWarn",
                value=f"Displays the history of warnings given to a user.\n{ctx.prefix}help userwarn",
                inline=False)
            help_2.add_field(
                name="RemoveWarn",
                value=f"Removes one of, or all of, the warnings given to a user.\n{ctx.prefix}help removewarn",
                inline=False)
            help_2.add_field(
                name="Unmute",
                value=f"Unmutes a user, thus allowing then to type.\n{ctx.prefix}help unmute",
                inline=False)
            help_2.add_field(
                name="Mute",
                value=f"Stops the user from typing in the server PERMANENTLY (or until unmute).\n{ctx.prefix}help mute",
                inline=False)
            help_2.set_footer(text="Made by Frost! and Mercurius13 for Mainesia's server")
            help_2.color = nextcord.Color.random()

            help_3 = nextcord.Embed(title="Help")
            help_3.add_field(
                name="Nick",
                value=f"Change nicknames in the server by using this feature.\n{ctx.prefix}help nick",
                inline=False)
            help_3.add_field(
                name="Kick",
                value=f"Kicks the specified user from the server.\n{ctx.prefix}help kick",
                inline=False)
            help_3.add_field(
                name="Unban",
                value=f"Unbans users, obviously.\n{ctx.prefix}help unban",
                inline=False)
            help_3.add_field(
                name="Ban",
                value=f"Bans users, like, DUH.\n{ctx.prefix}help ban",
                inline=False)
            help_3.set_footer(text="Made by Frost! and Mercurius13 for Mainesia's server")
            help_3.color = nextcord.Color.random()

            buttons = [
                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                              disabled=True),
                create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                              disabled=True),
                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                              disabled=False),
                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                              disabled=False),
            ]
            action_row = create_actionrow(*buttons)

            message = await ctx.send(embed=help_1, components=[action_row])

            while True:
                try:
                    response: ComponentContext = await wait_for_component(self.bot, components=action_row,
                                                                          messages=message, timeout=300)
                    while response.author != ctx.author:
                        await response.reply("This ain't your button fool", hidden=True)
                        response: ComponentContext = await wait_for_component(self.bot, components=action_row,
                                                                              timeout=300)

                    if response.component['custom_id'] == "forward":
                        page += 1

                    elif response.component['custom_id'] == "back":
                        page -= 1

                    elif response.component['custom_id'] == "big_forward":
                        page = pages

                    elif response.component['custom_id'] == "big_back":
                        page = 1

                    if page == 1:
                        try:
                            buttons_left_disabled = [
                                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                              disabled=True),
                                create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                              disabled=True),
                                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                              disabled=False),
                            ]
                            action_row = create_actionrow(*buttons_left_disabled)
                            await response.edit_origin(embed=help_1, components=[action_row])
                        except:
                            pass
                    elif page == 2:
                        try:
                            buttons_normal = [
                                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                              disabled=False),
                            ]
                            action_row2 = create_actionrow(*buttons_normal)
                            await response.edit_origin(embed=help_2, components=[action_row2])

                        except:
                            pass

                    elif page == 3:
                        try:
                            buttons_right_disabled = [
                                create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                              disabled=False),
                                create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                              disabled=True),
                                create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                              disabled=True),
                            ]
                            action_row3 = create_actionrow(*buttons_right_disabled)
                            await response.edit_origin(embed=help_3, components=[action_row3])

                        except:
                            pass
                    pass
                except asyncio.TimeoutError:
                    response: ComponentContext = await wait_for_component(self.bot, components=action_row,
                                                                          messages=message)
                    buttons_all_disabled = [
                        create_button(style=ButtonStyle.blue, custom_id="big_back", emoji="⏪",
                                      disabled=True),
                        create_button(style=ButtonStyle.blue, custom_id="back", emoji="◀",
                                      disabled=True),
                        create_button(style=ButtonStyle.blue, custom_id="forward", emoji="▶",
                                      disabled=True),
                        create_button(style=ButtonStyle.blue, custom_id="big_forward", emoji="⏩",
                                      disabled=True),
                    ]
                    action_row = create_actionrow(*buttons_all_disabled)
                    await response.edit_origin(components=[action_row])

        elif command.lower() == 'nick':
            embed = nextcord.Embed(
                title="Help Nick",
                description="Nickname your friends anything you want!\nIt is WAY too easy to do so, with this command.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}nick @<membername> <nickname>\nNow see what you can come up with...",
                inline=True
            )
            embed.set_footer(
                text="Nasty surprise for the poor victim's names *sigh*")
            await ctx.send(embed=embed)

        elif command.lower() == 'afk':
            embed = nextcord.Embed(
                title="Help Afk",
                description="Use this to make people know that your are afk when they ping you.\nUseful to warn people about your afkness!",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}afk <reason>\nThis will solve a lot of afk problems...",
                inline=True
            )
            embed.set_footer(text="Why didn't we think of this be4?")
            await ctx.send(embed=embed)

        elif command.lower() == 'slowmode':
            embed = nextcord.Embed(
                title="Help Slowmode",
                description="Allows you to put or remove a slowmode in your channel.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}slowmode <timeinseconds>\nThat will stop the SPAMMERS",
                inline=True
            )
            embed.set_footer(text="Sad life for spammers.")
            await ctx.send(embed=embed)

        elif command.lower() == 'blacklist':
            embed = nextcord.Embed(
                title="Help Blacklist",
                description="This makes the required member unable to use my commands.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}blacklist @<membername>\nThis is one of the most CRUELLEST punishments possible.",
                inline=True
            )
            embed.set_footer(text="Not using CHAD be SAD")
            await ctx.send(embed=embed)

        elif command.lower() == 'unblacklist':
            embed = nextcord.Embed(
                title="Help Unblacklist",
                description="Removes blacklisted users from the list of naughty people...",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}unblacklist @<membername>\nOnly kindness can make you use this command.",
                inline=True
            )
            embed.set_footer(text="Unblacklisters = Saviours")
            await ctx.send(embed=embed)

        elif command.lower() == 'clear':
            embed = nextcord.Embed(
                title="Help Clear",
                description="Clears the required number of messages in a channel. You can also clear messages of a particular member within a certain number of messages.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}clear <numberofmessages> <optionalmember>\nHelps when your server members just don't want to stop chatting...",
                inline=True
            )
            embed.set_footer(text="Get ERASED")
            await ctx.send(embed=embed)

        elif command.lower() == 'removewarn':
            embed = nextcord.Embed(
                title="Help RemoveWarn",
                description="Used to remove one or all of a users warn.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}removewarn <reason>\nGive the reason to remove, or just type 'all' to remove all warnings.",
                inline=True)
            embed.set_footer(text="Showing mercy gets you killed. You have been warned.")
            await ctx.send(embed=embed)

        elif command.lower() == 'warn':
            embed = nextcord.Embed(title="Help Warn",
                                   description="Gives the rule-breakers a warning!",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}warn <username> <reason>\nOnly for those naughty users who don't like rules.",
                inline=True
            )
            embed.set_footer(text="So you've been warned...")
            await ctx.send(embed=embed)

        elif command.lower() == 'userwarn':
            embed = nextcord.Embed(
                title="Help UserWarn",
                description="Gives a record of why and how many times a user was warned in the server.",
                color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}userwarn @<username>\nNow you have a record of their crimes.",
                inline=True
            )
            embed.set_footer(text="*Evil laughter from admins*")
            await ctx.send(embed=embed)

        elif command.lower() == 'unmute':
            embed = nextcord.Embed(title="Help Unmute",
                                   description="Allows you to unmute a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}unmute @<username>\nThis makes the able to talk in your server again.",
                inline=True
            )
            embed.set_footer(text="Support Freedom of Speech")
            await ctx.send(embed=embed)

        elif command.lower() == 'mute':
            embed = nextcord.Embed(title="Help Mute",
                                   description="Allows you to mute a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}mute @<username>\nNow they can't talk until you allow them too!",
                inline=True
            )
            embed.set_footer(text="Sad life for the muted")
            await ctx.send(embed=embed)

        elif command.lower() == 'kick':
            embed = nextcord.Embed(title="Help Kick",
                                   description="Allows you to kick a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}kick @<username>\nSo basically they just get yeeted out.",
                inline=True
            )
            embed.set_footer(text="Get rekt lol")
            await ctx.send(embed=embed)

        elif command.lower() == 'unban':
            embed = nextcord.Embed(title="Help Unban",
                                   description="Allows you to unban a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}unban @<username>\nSo that they can return to the server.",
                inline=True
            )
            embed.set_footer(text="Oh look, they're back lol")
            await ctx.send(embed=embed)

        elif command.lower() == 'ban':
            embed = nextcord.Embed(title="Help Ban",
                                   description="Allows you to ban a user.",
                                   color=nextcord.Color.green())
            embed.add_field(
                name="Usage:",
                value=f"{ctx.prefix}ban @<username>\nThey can NEVER COME BACK NOW MWA HA HA HA\nJeez I was only joking",
                inline=True
            )
            embed.set_footer(text="Get banished lmao")
            await ctx.send(embed=embed)

        else:
            embed = nextcord.Embed(
                title="Noice",
                description=f"You ask me for help, but I can't help you\nCause {command} isn't a part of my awesome features",
                color=nextcord.Color.green())
            embed.set_footer(text=f"Try {ctx.prefix}help without anything after it")
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Help(bot))
