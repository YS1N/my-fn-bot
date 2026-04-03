import fortnitepy
import os
from fortnitepy.ext import commands

# This pulls the login code from Mangoi's settings later
auth_code = os.getenv("AUTH_CODE")

bot = commands.Bot(
    command_prefix='!',
    auth=fortnitepy.AdvancedAuth(
        authorization_code=auth_code
    )
)

@bot.event
async def event_ready():
    print(f'Bot is online as {bot.user.display_name}')
    # Set default skin (Renegade Raider ID)
    await bot.user.set_outfit('CID_028_Athena_Commando_F_Rare')

@bot.event
async def event_friend_request(request):
    await request.accept()
    print(f'Accepted friend request from {request.display_name}')

# Keep this at the bottom
bot.run()
