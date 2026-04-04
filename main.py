import fortnitepy
import asyncio
import os

# 1. ANDROID CREDENTIALS (The ONLY ones currently working for you)
CID = "34a02cf8f4414e29b15921876da36f9a"
SECRET = "daafbA73L9z97CE0u85973795CD697CD"

async def run_bot():
    # 2. Get the secret code from Mangoi Environment Variables
    auth_code = os.getenv("AUTH_CODE")

    # 3. If NO code is found, show the ANDROID link
    if not auth_code:
        print("\n" + "!"*60)
        print("⚠️  ACTION REQUIRED: GET YOUR ANDROID LOGIN CODE ⚠️")
        print(f"https://www.epicgames.com/id/api/redirect?clientId={CID}&responseType=code")
        print("!"*60 + "\n")
        print("STEPS:")
        print("1. Open an INCOGNITO window.")
        print("2. Paste the link above and log in.")
        print("3. Copy the 32-character 'authorizationCode'.")
        print("4. Add it to Mangoi Settings as AUTH_CODE.")
        print("5. RESTART the bot.")
        return 

    # 4. If code IS found, attempt Android login
    print("🚀 AUTH_CODE detected! Attempting Android Login...")
    
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

    try:
        await client.start()
    except Exception as e:
        print(f"❌ LOGIN ERROR: {e}")
        print("💡 TIP: Your AUTH_CODE is expired. Delete it from Mangoi and get a NEW one!")

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"FATAL ERROR: {e}")
