from telethon import TelegramClient, events
import os

# Prendi le credenziali dalle variabili d'ambiente
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSION_NAME = "userbot_session"

# Avvia il client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

@client.on(events.NewMessage)  # Trigger per ogni nuovo messaggio ricevuto
async def handler(event):
    if event.is_private:  # Risponde solo ai messaggi privati
        await event.reply("Ciao! Sono un userbot su Heroku 🚀")

# Avvia il bot
client.start()
print("Userbot avviato!")
client.run_until_disconnected()
