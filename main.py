import fortnitepy
import asyncio
import os

# 1. NINTENDO SWITCH CREDENTIALS (The most stable ones)
CID = "852027419f8b46e3bb6d6e719602f04f"
SECRET = "f6705c7546a345679c17f0559a72175a"

async def run_bot():
    # 2. Check for the AUTH_CODE in Mangoi Environment Variables
    auth_code = os.getenv("AUTH_CODE")

    # 3. If NO code is found, show the NEW link and STOP
    if not auth_code:
        print("\n" + "!"*60)
        print("⚠️  ACTION REQUIRED: GET YOUR NINTENDO LOGIN CODE ⚠️")
        print(f"https://www.epicgames.com/id/api/redirect?clientId={CID}&responseType=code")
        print("!"*60 + "\n")
        print("STEPS TO FIX THE 'DISABLED' ERROR:")
        print("1. Open an INCOGNITO window (Ctrl+Shift+N).")
        print("2. Paste the link above and log in with the BOT account.")
        print("3. Copy the 32-character 'authorizationCode'.")
        print("4. Go to Mangoi Settings > Environment Variables.")
        print("5. Add Key: AUTH_CODE | Value: (Paste your NEW code).")
        print("6. RESTART the bot on Mangoi.")
        return 

    # 4. Attempt login with the new Switch Client
    print("🚀 AUTH_CODE detected! Attempting Nintendo Switch Login...")
    
    client = fortnitepy.Client(
        auth=fortnitepy.AdvancedAuth(
            authorization_code=auth_code
        )
    )

    @client.event
    async def event_ready():
        print("---------------------------------------")
        print(f"🔥 SUCCESS! Bot is online as: {client.user.display_name}")
        print("---------------------------------------")
        # Set skin to Renegade Raider
        await client.user.set_outfit('CID_028_Athena_Commando_F_Rare')

    @client.event
    async def event_friend_request(request):
        await request.accept()
        print(f"🤝 Accepted friend: {request.display_name}")

    # 5. Error Handling to prevent the "Death Loop"
    try:
        await client.start()
    except Exception as e:
        print(f"❌ LOGIN ERROR: {e}")
        print("💡 Your AUTH_CODE is old or for the wrong client. Reset it in Mangoi!")

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"FATAL SYSTEM ERROR: {e}")
