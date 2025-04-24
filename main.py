from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os

# Carregar variáveis do .env
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Olá! Eu sou o FURIABot, seu companheiro da torcida FURIA no Telegram!")

# Configuração do app
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # Adiciona o handler do /start
    app.add_handler(CommandHandler("start", start))

    print("✅ Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()
