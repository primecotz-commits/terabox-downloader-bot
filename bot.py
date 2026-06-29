from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

# ======== CHANGE THESE ========
BOT_TOKEN = 
ADMIN_ID = 5565826679
CHANNEL_USERNAME = "@Gezx_botz"
# ==============================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "»Hᴇʏ! {mention}
Wᴇʟᴄᴏᴍᴇ ᴛᴏ TᴇʀᴀBᴏx Dᴏᴡɴʟᴏᴀᴅᴇʀ Bᴏᴛ!

I ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ TᴇʀᴀBᴏx / 1024TᴇʀᴀBᴏx ғɪʟᴇ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴅɪʀᴇᴄᴛʟʏ ᴛᴏ ʏᴏᴜ — ɴᴏ ᴀᴘᴘs, ɴᴏ ᴀᴄᴄᴏᴜɴᴛs, ɴᴏ ʜᴀssʟᴇ.

✨ Fᴇᴀᴛᴜʀᴇs:
  • Fᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅs ᴠɪᴀ ᴀʀɪᴀ2
  • Sᴍᴀʀᴛ ᴄᴀᴄʜɪɴɢ — sᴀᴍᴇ ʟɪɴᴋ = ɪɴsᴛᴀɴᴛ ᴅᴇʟɪᴠᴇʀʏ
  • Sᴜᴘᴘᴏʀᴛs ᴠɪᴅᴇᴏ, ᴅᴏᴄᴜᴍᴇɴᴛs, ɪᴍᴀɢᴇs & ᴍᴏʀᴇ
  • Sᴛʀᴇᴀᴍ ʟɪɴᴋs ғᴏʀ ʟᴀʀɢᴇ ғɪʟᴇs

Jᴜsᴛ sᴇɴᴅ ᴀɴʏ TᴇʀᴀBᴏx ʟɪɴᴋ ᴛᴏ ɢᴇᴛ sᴛᴀʀᴛᴇᴅ!"
    )


async def terabox_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "terabox.com" in text or "1024tera.com" in text:
        await update.message.reply_text(
            "✅ TeraBox link detected.\n\n"
            "⏳ Download feature will be added in the next step."
        )
    else:
        await update.message.reply_text(
            "❌ Pʟᴇᴀsᴇ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴘᴜʙʟɪᴄ TᴇʀᴀBᴏx ʟɪɴᴋ!"
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, terabox_link)
    )

    print("Bot Started...")
    app.run_polling()


if name == "main":
    main()
