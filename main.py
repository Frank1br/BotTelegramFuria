import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import re


load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Função para escapar caracteres do Markdown V2
def escapar_markdown_v2(texto: str) -> str:
    return re.sub(r'([_*\[\]()~`>#+\-=|{}.!\\])', r'\\\1', texto)

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = "👋 Olá! Eu sou o FURIABot, seu companheiro da torcida FURIA no Telegram!"
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /proximojogo
async def proximo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🎮 Próximo Jogo da FURIA!\n\n"
        "🗓 Data: 05/05/2025\n"
        "⏰ Horário: 18h00\n"
        "🆚 Adversário: Team Vitality\n"
        "📍 Torneio: BLAST Premier Spring\n\n"
        "Vai pra cima deles, FURIA!"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /historia
async def historia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🔥 A FURIA foi fundada em 2017 e rapidamente se destacou no cenário de esports.\n\n"
        "Com paixão, estratégia e muita garra, a equipe conquistou fãs ao redor do mundo, "
        "especialmente no CS:GO, onde brilhou em torneios internacionais.\n\n"
        "Hoje, a FURIA representa não só um time, mas um movimento feroz de competitividade!"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Inicialização do bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("proximojogo", proximo_jogo))
    app.add_handler(CommandHandler("historia", historia))

    print("✅ Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()
