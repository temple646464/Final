
import os
from pyrogram import Client, filters
import requests

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("BOT_OWNER_ID"))
UPLOADER_URL = os.getenv("UPLOADER_URL")

app = Client("bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.document & filters.private)
async def handle_txt_file(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply("You're not authorized to use this bot.")
        return

    if not message.document.file_name.endswith(".txt"):
        await message.reply("Please send a .txt file.")
        return

    file_path = await message.download()
    with open(file_path, "rb") as f:
        files = {'file': (message.document.file_name, f)}
        response = requests.post(UPLOADER_URL, files=files)

    if response.ok:
        data = response.json()
        await message.reply_text(f"Uploaded `{data['filename']}` successfully.\nContent:\n{data['content'][:1000]}")
    else:
        await message.reply_text("Upload failed.")

app.run()
