import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

intents = discord.Intents.default()
intents.members = True  # Enable member intents

bot = commands.Bot(command_prefix='!', intents=intents)

# Replace these with your role IDs and corresponding messages
ROLE_MESSAGES = {
    1005887535567868057: """
hii! thank you for subscribing to legend!! these are some of the perks the subscription has:

・create custom voice channels by joining https://discord.com/channels/679875946597056683/1120219024882675732
・stream and video access in voice channels
・image, embed, reaction and sticker perms
・access to <#683948567215472640>

the role also gives you access to chat with me as much as you'd like! i can assist in answering your questions, helping with issues or just chat about your interests! thank you for subscribing  ⸜(ˊᗜˋ)⸝""",
    1031542676048314388: """
hii! thank you for subscribing to champion!! these are some of the perks the subscription has:

・create a custom role
‏‏‎ ‎‏‏‎ ‎✎... can be set up using `/titan-role edit`
・featured on the memberlist
・create custom voice channels by joining https://discord.com/channels/679875946597056683/1120219024882675732
・stream and video access in voice channels
・image, embed, reaction and sticker perms
・access to <#683948567215472640>

the role also gives you access to chat with me as much as you'd like! i can assist in answering your questions, helping with issues or just chat about your interests! thank you for subscribing  ⸜(ˊᗜˋ)⸝""",
    1162013585652850778: """
hii! thank you for subscribing to titan!! these are some of the perks the subscription has:

・create your own clan
‏‏‎ ‎‏‏‎ ‎✎... can be set up using `/clan create`
・create a custom role
‏‏‎ ‎‏‏‎ ‎✎... can be set up using `/titan-role edit`
・gift a subcription
‏‏‎ ‎‏‏‎ ‎✎... gift it to a friend with `/titan-role gift-legend`
・featured on the memberlist
・create custom voice channels by joining https://discord.com/channels/679875946597056683/1120219024882675732
・stream and video access in voice channels
・image, embed, reaction and sticker perms
・access to <#683948567215472640>

the role also gives you access to chat with me as much as you'd like! i can assist in answering your questions, helping with issues or just chat about your interests! thank you for subscribing  ⸜(ˊᗜˋ)⸝""",
    1004781656969846805: """
hii! thank you for subscribing to legend!! these are some of the perks the subscription has:

・create custom voice channels by joining https://discord.com/channels/828370043867496531/1006294611498643637
・stream and video access in voice channels
・access to <#1006197353226711150>
・make ur rank role show
‏‏‎ ‎‏‏‎ ‎✎... show it with `/toggle-rank`

the role also gives you access to chat with me as much as you'd like! i can assist in answering your questions, helping with issues or just chat about your interests! thank you for subscribing  ⸜(ˊᗜˋ)⸝""",
    1087725163178622998: """
hii! thank you for subscribing to champion!! these are some of the perks the subscription has:

・create a custom role
‏‏‎ ‎‏‏‎ ‎✎... can be set up using `/titan-role edit`
・featured on the memberlist
・create custom voice channels by joining https://discord.com/channels/828370043867496531/1006294611498643637
・soundboard access
・stream and video access in voice channels
・access to <#1006197353226711150>
・make ur rank role show
‏‏‎ ‎‏‏‎ ‎✎... show it with `/toggle-rank`

the role also gives you access to chat with me as much as you'd like! i can assist in answering your questions, helping with issues or just chat about your interests! thank you for subscribing  ⸜(ˊᗜˋ)⸝""",
    1161640076745375786: """
hii! thank you for subscribing to titan!! these are some of the perks the subscription has:

・create your own clan
‏‏‎ ‎‏‏‎ ‎✎... can be set up using `/clan create`
・custom role
‏‏‎ ‎‏‏‎ ‎✎... can be set up using `/titan-role edit`
・free legend sub gift
‏‏‎ ‎‏‏‎ ‎✎... gift it to a friend with `/titan-role gift-legend`
・shown on the sidebar
・custom voice channels
・soundboard access
・stream and video access in voice channels
・access to <#1006197353226711150>
・make ur rank role show
‏‏‎ ‎‏‏‎ ‎✎... show it with `/toggle-rank`

the role also gives you access to chat with me as much as you'd like! i can assist in answering your questions, helping with issues or just chat about your interests! thank you for subscribing  ⸜(ˊᗜˋ)⸝"""
}

@bot.event
async def on_ready():
    print(f'Bot is ready! Logged in as {bot.user.name}')

@bot.event
async def on_member_update(before, after):
    # Check if roles were added
    new_roles = set(after.roles) - set(before.roles)
    
    if new_roles:  # If any roles were added
        for role in new_roles:
            if role.id in ROLE_MESSAGES:
                try:
                    # Send DM to the user
                    await after.send(ROLE_MESSAGES[role.id])
                except discord.Forbidden:
                    # If user has DMs disabled
                    print(f"Couldn't send DM to {after.name}")

# Get token from environment variables
bot.run(os.getenv('DISCORD_BOT_TOKEN'))
