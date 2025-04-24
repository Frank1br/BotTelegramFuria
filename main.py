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
    mensagem = (
        "👊 *E AÍ, TORCEDOR DA FURIA!*\n\n"
        "🔥 *Eu sou o FURIABot* 🔥\n"
        "🖤💛 Seu companheiro da torcida FURIA aqui no Telegram! Vamos juntos apoiar a nossa bandeira e gritar pelos nossos! 💥\n"
        "🎮 Fique ligado em tudo sobre os jogos, resultados e notícias.\n\n"
        "*Vamos invadir a arena e dominar o jogo!* ⚔️\n"
        "_#FURIA #CSGO #GoFURIA_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /proximojogo
async def proximo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🔥 *FURIA NA ÁREA, PREPARE\-SE!* 🔥\n\n"
        "🎮 *Próximo Jogo da FURIA!*\n"
        "🗓 *Data:* 05\\/05\\/2025\n"
        "⏰ *Horário:* 18h00\n"
        "🆚 *Adversário:* Team Vitality\n"
        "📍 *Torneio:* BLAST Premier Spring\n\n"
        "💣 *Vai pra cima deles, FURIA!* 💛🖤\n"
        "_#DIADEFURIA  #GOFURIA  #CS2_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /historia
async def historia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "💥 *HISTÓRIA DA FURIA* 💥\n\n"
        "🎮 *O COMEÇO DA LENDÁRIA FURIA!* 🏆\n"
        "A FURIA nasceu com um objetivo claro: dominar o cenário competitivo! Desde o início, com sua força imbatível e espírito guerreiro, conquistaram as maiores vitórias do CS:GO, sendo a primeira organização brasileira a quebrar barreiras no cenário internacional! 💛🖤\n\n"
        "🔥 *Com um time campeão e a torcida mais apaixonada do mundo, FURIA é o símbolo de luta, garra e superação!* 🔥\n"
        "E essa história tá só começando, meu amigo! Vamos juntos para mais vitórias! ⚡\n"
        "_#GoFURIA #RaizDaTorcida #FURIACampeã_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /Razao
async def furiaRazao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🔥 *POR QUE AMAMOS A FURIA?* 🔥\n\n"
        "🖤💛 *A FURIA é nossa paixão, é o nosso orgulho!*\n"
        "Cada jogada, cada vitória, é um motivo para gritar até perder a voz! 💥💣\n\n"
        "🏆 Desde o começo, eles provaram que, no CS:GO, não existem limites! A FURIA não é só uma equipe, é a nossa essência de luta, superação e união! 💪\n"
        "Com a nossa torcida apaixonada, não tem como dar errado! 💥\n\n"
        "🔥 *Juntos, somos mais fortes!* 🔥\n"
        "_#FURIA #GoFURIA #UnidosPeloCampeonato_"
    )
    mensagem_escapada = escapar_markdown_v2(mensagem)
    await update.message.reply_markdown_v2(mensagem_escapada)

# Comando /Recordes    
async def furiaRecordes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "💥 *RECORDES DA FURIA QUE MARCARAM A HISTÓRIA!* 💥\n\n"
        "🏆 *A FURIA é uma máquina de quebrar recordes!* 🏆\n"
        "Da *BLAST Premier* ao *CS:GO Major*, eles têm dominado tudo!\n"
        "🔥 Com a nossa torcida em peso, eles conquistam vitórias imbatíveis!\n\n"
        "*Recordes incríveis como:* \n"
        "🏅 *Maior número de vitórias em torneios internacionais* 🌍\n"
        "🏅 *A melhor equipe do Brasil no CS:GO* 🇧🇷\n\n"
        "🔥 *Esses recordes são apenas o começo. FURIA, a caminho de mais conquistas!* 🔥\n"
        "_#FURIA #Recordes #GoFURIA_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /futuro
async def furiaFuturo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "⚡ O FUTURO DA FURIA É BRILHANTE! ⚡\n\n"
        "🔮 O que vem por aí para a nossa FURIA? *Conquistas, vitórias e mais histórias épicas!* 🚀\n\n"
        "A FURIA não para de crescer, com novos talentos, novas competições e mais força! 🔥💪\n"
        "💛🖤 O time vai continuar arrebentando no cenário e a nossa torcida vai ficar ainda mais insana!\n\n"
        "*O futuro da FURIA é agora e é *nossa* história a ser escrita!* 🖊️💥\n"
        "_#GoFURIA #FuturoDaFURIA #CS2_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Inicialização do bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("proximojogo", proximo_jogo))
    app.add_handler(CommandHandler("historia", historia))
    app.add_handler(CommandHandler("razao", furiaRazao))
    app.add_handler(CommandHandler("recordes", furiaRecordes))
    app.add_handler(CommandHandler("futuro", furiaFuturo))

    print("✅ Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()
