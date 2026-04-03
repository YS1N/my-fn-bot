import fortnitepy
import asyncio
import os

# 1. Configuration (Epic Games Launcher Credentials)
CID = "34a02cf8f4414e29b15921876da36f9a"
SECRET = "daafbA73L9z97CE0u85973795CD697CD"

async def run_bot():
    # 2. Check for the AUTH_CODE in Mangoi Environment Variables
    auth_code = os.getenv("AUTH_CODE")

    # 3. If no code is found, show the link and STOP (to prevent crashing)
    if not auth_code:
        print("\n" + "!"*50)
        print("⚠️ ACTION REQUIRED: GET YOUR LOGIN CODE ⚠️")
        print(f"https://www.epicgames.com/id/api/redirect?clientId={CID}&responseType=code")
        print("!"*50 + "\n")
        print("STEPS:")
        print("1. Click the link above and log in to your Bot Account.")
        print("2. Copy the 32-character 'authorizationCode' from the white page.")
        print("3. Go to Mangoi Settings > Environment Variables.")
        print("4. Add Key: AUTH_CODE | Value: (Paste your 32-digit code).")
        print("5. RESTART the bot on Mangoi.")
        return 

    # 4. If code IS found, log in normally
    print("🚀 AUTH_CODE detected! Attempting to log in to Fortnite...")
    
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
        # Sets skin to Renegade Raider (Default)
        await client.user.set_outfit('CID_028_Athena_Commando_F_Rare')

    @client.event
    async def event_friend_request(request):
        await request.accept()
        print(f"🤝 Accepted friend request from: {request.display_name}")

    # 5. Start the engine
    try:
        await client.start()
    except Exception as e:
        print(f"❌ LOGIN ERROR: {e}")
        print("💡 Your AUTH_CODE probably expired. Delete it from Mangoi and get a new one!")

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass
