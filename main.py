import fortnitepy
import os
import asyncio
from fortnitepy.ext import commands

# This pulls the login code from Mangoi's settings
auth_code = os.getenv("AUTH_CODE")

async def run_bot():
    # Setup the bot inside the async function to fix the loop error
    bot = commands.Bot(
        command_prefix='!',
        auth=fortnitepy.AdvancedAuth(
            authorization_code=auth_code
        )
    )

    @bot.event
    async def event_ready():
        print(f'✅ Bot is online as {bot.user.display_name}')
        # Set default skin (Renegade Raider ID)
        await bot.user.set_outfit('CID_028_Athena_Commando_F_Rare')

    @bot.event
    async def event_friend_request(request):
        await request.accept()
        print(f'🤝 Accepted friend request from {request.display_name}')

    try:
        await bot.start()
    except Exception as e:
        print(f"❌ Error starting bot: {e}")

# This starts the async loop properly
if __name__ == "__main__":
    asyncio.run(run_bot())
