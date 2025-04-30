
# Pyrogram Telegram Bot for TXT File Uploading

This bot receives `.txt` files via Telegram and uploads them to a public Flask-based uploader endpoint.

## Requirements

- Telegram API ID and API Hash (get from https://my.telegram.org)
- Telegram Bot Token (from @BotFather)
- Telegram User ID (for bot owner)
- Public URL of your uploader (hosted on Render or elsewhere)

## Usage

### 1. Create `.env` File

Copy the example:

```bash
cp .env.example .env
```

Edit `.env` and fill in your credentials.

### 2. Run with Docker

```bash
docker build -t pyrogram-txt-bot .
docker run --env-file .env pyrogram-txt-bot
```

### Environment Variables

| Variable       | Description                        |
|----------------|------------------------------------|
| `API_ID`       | Telegram API ID                    |
| `API_HASH`     | Telegram API Hash                  |
| `BOT_TOKEN`    | Bot token from BotFather           |
| `BOT_OWNER_ID` | Your personal Telegram user ID     |
| `UPLOADER_URL` | Public URL to the Flask uploader   |

Only the bot owner will be allowed to send files.

## License

MIT
