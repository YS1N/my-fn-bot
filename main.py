import fortnitepy
import os
import asyncio
from fortnitepy.ext import commands

# This tries to get the code from Mangoi settings
auth_code = os.getenv("AUTH_CODE")

async def run_bot():
    # If there's no code, we use a different way to log in so it doesn't crash
    if not auth_code:
        print("⚠️ No AUTH_CODE found in Settings. Starting manual login...")
        auth = fortnitepy.AdvancedAuth()
    else:
        print("✅ Found AUTH_CODE! Logging in...")
        auth = fortnitepy.AdvancedAuth(authorization_code=auth_code)

    bot = commands.Bot(
        command_prefix='!',
        auth=auth
    )

    @bot.event
    async def event_ready():
        print(f'🔥 Bot is ONLINE as {bot.user.display_name}')
        await bot.user.set_outfit('CID_028_Athena_Commando_F_Rare')

    @bot.event
    async def event_friend_request(request):
        await request.accept()

    try:
        await bot.start()
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    asyncio.run(run_bot())
