import fortnitepy
import asyncio
import os
import sys

# 1. Get the secret code from Mangoi Environment Variables
auth_code = os.getenv("AUTH_CODE")

async def run_bot():
    print("--- 🚀 FORTNITE BOT STARTING 🚀 ---")

    # 2. Decide how to log in
    if not auth_code or auth_code == "":
        print("⚠️ WARNING: No AUTH_CODE found in Mangoi Settings.")
        print("👉 LOOK BELOW FOR THE LOGIN LINK! 👇")
        # This forces the library to print the login link to the logs
        auth = fortnitepy.AdvancedAuth()
    else:
        print(f"✅ AUTH_CODE detected! Attempting to log in...")
        auth = fortnitepy.AdvancedAuth(
            authorization_code=auth_code
        )

    # 3. Setup the Client
    client = fortnitepy.Client(
        auth=auth,
        status="Mangoi 24/7 Bot"
    )

    @client.event
    async def event_ready():
        print("---------------------------------------")
        print(f"🔥 SUCCESS! Bot is online as: {client.user.display_name}")
        print("---------------------------------------")
        # Sets skin to Renegade Raider by default
        await client.user.set_outfit('CID_028_Athena_Commando_F_Rare')

    @client.event
    async def event_friend_request(request):
        await request.accept()
        print(f"🤝 Accepted friend: {request.display_name}")

    # 4. Start the bot and catch errors
    try:
        await client.start()
    except Exception as e:
        print(f"❌ ERROR STARTING BOT: {e}")
        print("💡 TIP: If it says 'NoneType', you need a NEW auth code from the link.")

# 5. Run the background loop
if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(run_bot())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"FATAL ERROR: {e}")
