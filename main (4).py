import discord
from discord.ext import commands

import datetime
import random
import requests

Intents = discord.Intents.all()
client = discord.Client(intents=Intents)

tree = discord.app_commands.CommandTree(client)

# SETUP
welcome_channel = #your welcome channel id
leave_channel = #Your leave channel id
verify_role = #Your verify role id
TOKEN = #Your Token

@tree.command(name="ping", description="Ping the bot!")
async def ping(ctx):
  embed = discord.Embed(
    title = "Recieved!",
    description = f"It took {round(client.latency * 1000)}ms to respond!",
    color = discord.Color.green()
  )
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /ping.")

@tree.command(name="verify", description="Verify yourself to the server!")
async def verify(ctx):
  if verify_role:
    if verify_role and discord.utils.get(ctx.user.roles, id=int(verify_role)):
      await ctx.response.send_message("You are already verified!")
    else:
      await ctx.user.add_roles(discord.utils.get(ctx.guild.roles, id=int(verify_role)))
    embed = discord.Embed(
      title="Verified!",
      description="You have been verified!",
      color=discord.Color.green()
    )
    await ctx.response.send_message(embed=embed)
  else:
    embed = discord.Embed(
      title="Error!",
      description="The verify role is not set!",
      color=discord.Color.red()
    )
    await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /verify.")

@tree.command(name="ban" , description="Ban a user from the server!")
async def ban(ctx, user: discord.Member, reason: str = None):
  if ctx.user.guild_permissions.ban_members:
    await user.ban(reason=reason)
    embed = discord.Embed(
      title = "Banned!",
      color = discord.Color.green()
    )
    embed.add_field(name="User", value=user.mention)
    embed.add_field(name="Reason", value=reason)
    await ctx.response.send_message(embed=embed)
  else:
    embed = discord.Embed(
      title = "Error!",
      description = "You don't have permission to ban members!",
      color = discord.Color.red()
    )
    await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /ban.")

@tree.command(name="kick", description="Kick a user from the server!")
async def kick(ctx, user: discord.Member, reason: str = None):
  if ctx.user.guild_permissions.kick_members:
    await user.kick(reason=reason)
    embed = discord.Embed(
      title = "Kicked!",
      color = discord.Color.green()
    )
    embed.add_field(name="User", value=user.mention)
    embed.add_field(name="Reason", value=reason)
    await ctx.response.send_message(embed=embed)
  else:
    embed = discord.Embed(
      title = "Error!",
      description = "You don't have permission to kick members!",
      color = discord.Color.red()
    )
    await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /kick.")

@tree.command(name="unban", description="Unban a user from the server!")
async def unban(ctx, user: discord.User, reason: str = None):
  if ctx.user.guild_permissions.ban_members:
    await ctx.guild.unban(user, reason=reason)
    embed = discord.Embed(
      title = "Unbanned!",
      color = discord.Color.green()
    )
    embed.add_field(name="User", value=user.mention)
    embed.add_field(name="Reason", value=reason)
    await ctx.response.send_message(embed=embed)
  else:
    embed = discord.Embed(
      title = "Error!",
      description = "You don't have permission to unban members!",
      color = discord.Color.red()
    )
    await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /unban.")

@tree.command(name="purge", description="Purge a certain amount of messages from the channel!")
async def purge(ctx, *, amount: int):
  if ctx.user.guild_permissions.manage_messages:
    await ctx.channel.purge(limit=amount)
    embed = discord.Embed(
      title = "Purged!",
      color = discord.Color.green()
    )
    embed.add_field(name="Amount", value=amount)
    await ctx.response.send_message(embed=embed)
  else:
    embed = discord.Embed(
      title = "Error!",
      description = "You don't have permission to purge messages!",
      color = discord.Color.red()
    )
    await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /purge.")

@tree.command(name="rpc", description="Play rock paper scissors with the bot!")
async def rpc(ctx, choice: str):
  bot_choice = random.choice(["rock", "paper", "scissors"])
  if choice == "rock":
    if bot_choice == "rock":
      await ctx.response.send_message(f"I chose {bot_choice}! It's a tie!")
    elif bot_choice == "paper":
      await ctx.response.send_message(f"I chose {bot_choice}! I win!")
    elif bot_choice == "scissors":
      await ctx.response.send_message(f"I chose {bot_choice}! You win!")
  elif choice == "paper":
    if bot_choice == "rock":
      await ctx.response.send_message(f"I chose {bot_choice}! You win!")
    elif bot_choice == "paper":
      await ctx.response.send_message(f"I chose {bot_choice}! It's a tie!")
    elif bot_choice == "scissors":
      await ctx.response.send_message(f"I chose {bot_choice}! I win!")
  elif choice == "scissors":
    if bot_choice == "rock":
      await ctx.response.send_message(f"I chose {bot_choice}! I win!")
    elif bot_choice == "paper":
      await ctx.response.send_message(f"I chose {bot_choice}! You win!")
    elif bot_choice == "scissors":
      await ctx.response.send_message(f"I chose {bot_choice}! It's a tie!")
  else:
    await ctx.response.send_message("Invalid choice! Please choose rock, paper, or scissors.")
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /rpc.")

@tree.command(name="8ball", description="Ask the magic 8 ball a question!")
async def eightball(ctx, question: str):
  answer = random.choice(["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."])
  embed = discord.Embed(
    title = "Magic 8 Ball",
    color = discord.Color.green()
  )
  embed.add_field(name="Question", value=question)
  embed.add_field(name="Answer", value=answer)
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /8ball.")

@tree.command(name="coinflip", description="Flip a coin!")
async def coinflip(ctx):
  result = random.choice(["Heads", "Tails"])
  embed = discord.Embed(
    title = "Coin Flip",
    description = f"The coin landed on {result}!",
    color = discord.Color.random()
  )
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /coinflip.")

@tree.command(name="roll", description="Roll a dice!")
async def roll(ctx):
  result = random.randint(1, 6)
  embed = discord.Embed(
    title = "Dice Roll",
    description = f"You rolled a {result}!",
    color = discord.Color.random()
  )
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /roll.")

@tree.command(name="meme", description="Get a random meme!")
async def meme(ctx):
        #vars
        response = requests.get("https://api.imgflip.com/get_memes")
        data = response.json()
        memes = data["data"]["memes"]
        random_meme = memes[random.randint(0, len(memes)-1)]
        meme_url = random_meme["url"]
        #Embed
        embed = discord.Embed(
          title = "Zufälliges Meme",
          color = discord.Color.random()
        )
        embed.set_image(
          url = meme_url
        )
        embed.set_footer(
          text = f"Requested by {ctx.user.name}"
        )
        await ctx.response.send_message(embed=embed)
        with open('log.txt', 'a') as file:
          file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /meme.")

@tree.command(name="serverinfo", description="Get information about the server!")
async def serverinfo(ctx):
  server = ctx.guild
  embed = discord.Embed(
    title = "Server Info",
    color = discord.Color.random()
  )
  embed.add_field(name="Name", value=server.name)
  embed.add_field(name="ID", value=server.id)
  embed.add_field(name="Owner", value=server.owner)
  embed.add_field(name="Members", value=server.member_count)
  embed.add_field(name="Created At", value=server.created_at)
  embed.add_field(name="Verification Level", value=server.verification_level)
  embed.add_field(name="Boosts", value=server.premium_subscription_count)
  embed.add_field(name="Boost Level", value=server.premium_tier)
  embed.add_field(name="Channels", value=len(server.channels))
  embed.add_field(name="Roles", value=len(server.roles))
  embed.add_field(name="Emojis", value=len(server.emojis))
  embed.add_field(name="members" , value=len(server.members))
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /serverinfo.")

@tree.command(name="userinfo", description="Get information about a user!")
async def userinfo(ctx, user: discord.Member):
  embed = discord.Embed(
    title = "User Info",
    color = discord.Color.random()
  )
  embed.add_field(name="Name", value=user.name)
  embed.add_field(name="ID", value=user.id)
  embed.add_field(name="Created At", value=user.created_at)
  embed.add_field(name="Joined At", value=user.joined_at)
  embed.add_field(name="Roles", value=", ".join([role.name for role in user.roles]))
  embed.add_field(name="Top Role", value=user.top_role)
  embed.add_field(name="Bot", value=user.bot)
  embed.add_field(name="Nickname", value=user.nick)
  embed.add_field(name="Avatar", value=user.avatar)
  embed.add_field(name="Banner", value=user.banner)
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /userinfo.")

@tree.command(name="avatar", description="Get the avatar of a user!")
async def avatar(ctx, user: discord.Member):
  embed = discord.Embed(
    title = "Avatar",
    color = discord.Color.random()
  )
  embed.set_image(url=user.avatar)
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /avatar.")

@tree.command(name="info", description="Get information about the bot!")
async def info(ctx):
  embed = discord.Embed(
    title = "Bot Info",
    color = discord.Color.random()
  )
  embed.add_field(name="Name", value=client.user.name)
  embed.add_field(name="ID", value=client.user.id)
  embed.add_field(name="Created At", value=client.user.created_at)
  embed.add_field(name="Prefix", value="/")
  embed.add_field(name="Commands", value=len(tree.get_commands()))
  embed.add_field(name="Servers", value=len(client.guilds))
  embed.add_field(name="Users", value=len(client.users))
  await ctx.response.send_message(embed=embed)
  with open('log.txt', 'a') as file:
    file.write(f"\n[{datetime.datetime.now()}] {ctx.user} used /info.")

@client.event
async def on_voice_state_update(member, before, after):
  if before.channel is None and after.channel is not None:
    with open('log.txt', 'a') as file:
        file.write(f"\n[{datetime.datetime.now()}] {member} joined voice channel {after.channel}.")
  elif after.channel is None and before.channel is not None:
    with open('log.txt', 'a') as file:
      file.write(f"\n[{datetime.datetime.now()}] {member} left voice channel {before.channel}.")

@client.event
async def on_member_join(member):
  channel = client.get_channel(welcome_channel)
  embed = discord.Embed(
    title = f"Welcome to {member.guild.name}!",
    description = f"Welcome {member.mention} to the server! We hope you have a great time here!",
    color = discord.Color.random()
  )
  embed.set_thumbnail(url=member.avatar.url)
  embed.set_footer(text=f"We are now at {member.guild.member_count} members!")
  await channel.send(embed=embed)
  with open("log.txt", "a") as file:
    file.write(f"\n[{datetime.datetime.utcnow}] {member.name} joined the server")

@client.event
async def on_member_remove(member):
  channel = client.get_channel(leave_channel)
  embed = discord.Embed(
    title = f"{member.name} left the server!",
    description = f"{member.mention} just left the server. We hope to see them again soon!",
    color = discord.Color.red()
  )
  embed.set_footer(text=f"We are now at {member.guild.member_count} members!")
  await channel.send(embed=embed)
  with open("log.txt", "a") as file:
    file.write(f"\n[{datetime.datetime.utcnow}] {member.name} left the server")

@client.event
async def on_ready():
  await tree.sync()
  print("Ready!")
  with open("log.txt", "a") as file:
    file.write(f"\n[{datetime.datetime.utcnow}] Bot started")

client.run(TOKEN)