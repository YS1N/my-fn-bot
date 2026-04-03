import fortnitepy
import asyncio
import os

# 1. New IOS Launcher Credentials (Fixes 'client_disabled' error)
CID = "34a02cf8f4414e29b15921876da36f9a"
SECRET = "daafbA73L9z97CE0u85973795CD697CD"

# If the one above fails, the bot will use the second most common one automatically
async def run_bot():
    # 2. Get the secret code from Mangoi Environment Variables
    auth_code = os.getenv("AUTH_CODE")

    # 3. If NO code is found, show the login box and stop
    if not auth_code:
        print("\n" + "!"*50)
        print("⚠️ ACTION REQUIRED: NEW LOGIN LINK ⚠️")
        print(f"https://www.epicgames.com/id/api/redirect?clientId={CID}&responseType=code")
        print("!"*50 + "\n")
        print("STEPS:")
        print("1. Open an INCOGNITO/PRIVATE window.")
        print("2. Paste the link above and log in with the BOT account.")
        print("3. Copy the 32-character 'authorizationCode'.")
        print("4. Add it to Mangoi Settings as AUTH_CODE.")
        print("5. RESTART the bot.")
        return 

    # 4. If code IS found, attempt login
    print("🚀 AUTH_CODE detected! Attempting to log in...")
    
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
        # Renegade Raider Outfit
        await client.user.set_outfit('CID_028_Athena_Commando_F_Rare')

    @client.event
    async def event_friend_request(request):
        await request.accept()
        print(f"🤝 Accepted friend: {request.display_name}")

    try:
        await client.start()
    except Exception as e:
        print(f"❌ LOGIN ERROR: {e}")
        print("💡 TIP: Delete the AUTH_CODE from Mangoi and get a NEW one from the link.")

if __name__ == "__main__":
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        pass
