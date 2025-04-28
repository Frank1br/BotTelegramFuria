import os
import random
import re
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")

# Função para escapar caracteres do Markdown V2
def escapar_markdown_v2(texto: str) -> str:
    return re.sub(r'([_\[\]()~`>#+\-=|{}.!\\])', r'\\\1', texto)

# Dados do time da FURIA
time_furia = [
    {
        "nome": "Fallen",
        "funcao": "AWPer / IGL",
        "imagem": "https://img-cdn.hltv.org/playerbodyshot/Wf26SO_o8nvnsLh0AqZXc5.png?ixlib=java-2.1.0&w=400&s=36b7189a4ae7b020d0acb087fd44777a"
    },
    {
        "nome": "Yuurih",
        "funcao": "Rifler",
        "imagem": "https://img-cdn.hltv.org/playerbodyshot/i6UGhkYxrhutAOmWZT0-8O.png?ixlib=java-2.1.0&w=400&s=2cd696f6ff4baf5680a43d537214b6eb"
    },
    {
        "nome": "Yekindar",
        "funcao": "Entry Fragger",
        "imagem": "https://img-cdn.hltv.org/playerbodyshot/rRclDPBXIMxFv2fv0dV0J0.png?ixlib=java-2.1.0&w=400&s=2b0f6209ca40efa081852b9d1d8e01c1"
    },
    {
        "nome": "Kserato",
        "funcao": "Rifler",
        "imagem": "https://img-cdn.hltv.org/playerbodyshot/U6t0j2bJDKUR3mTI8rIqv7.png?ixlib=java-2.1.0&w=400&s=b5257c378b8122f415f21985855e95ca"
    },
    {
        "nome": "Molody",
        "funcao": "Support",
        "imagem": "https://img-cdn.hltv.org/playerbodyshot/qNyAd_xVHTTmbCAKPx-jPk.png?ixlib=java-2.1.0&w=400&s=b128ede878e462107c70590202b14139"
    },
]

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    redes_sociais = (
        "🌐 Siga a FURIA nas redes sociais: \n"
        " Instagram: https://www.instagram.com/furiagg/ \n"
        " Twitter: https://twitter.com/FURIA \n"
        " YouTube: https://www.youtube.com/c/FURIA \n\n"
    )
    if args and args[0] == "csgo":
        mensagem = redes_sociais + (
            "🎯 Bem-vindo, guerreiro da FURIA! \n\n"
            "Você chegou direto do link secreto da comunidade CS:GO! 😎🔥\n"
            "Preparado para acompanhar todos os passos do nosso time?\n"
            "Vamos nessa! 💣💥"
        )
    else:
        mensagem = redes_sociais + (
            "👊 E AÍ, TORCEDOR DA FURIA!\n\n"
            "🔥 Eu sou o FURIABot 🔥\n"
            "🖤💛 Seu companheiro da torcida FURIA aqui no Telegram! Vamos juntos apoiar a nossa bandeira e gritar pelos nossos! 💥\n"
            "🎮 Fique ligado em tudo sobre os jogos, resultados e notícias.\n\n"
            "Vamos invadir a arena e dominar o jogo! ⚔️\n"
            "_#FURIA #CSGO #GoFURIA_\n\n"
            "📝 Comandos disponíveis:\n"
            "/start - Inicia a conversa com o bot\n"
            "/proximojogo - Mostra o próximo jogo da FURIA\n"
            "/historia - Conta a história da FURIA\n"
            "/razao - Por que amamos a FURIA\n"
            "/recordes - Recordes da FURIA\n"
            "/futuro - O futuro da FURIA\n"
            "/membros - Conheça nosso time de maneira aleatoria 🖤🔥\n"
            "/torcaconosco - Poste torcendo pela FURIA"
        )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /proximojogo
async def proximo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🔥 FURIA NA ÁREA, PREPARE\-SE! 🔥\n\n"
        "🎮 Próximo Jogo da FURIA!\n"
        "🗓 Data: 05\\/05\\/2025\n"
        "⏰ Horário: 18h00\n"
        "🆚 Adversário: Team Vitality\n"
        "📍 Torneio: BLAST Premier Spring\n\n"
        "💣 Vai pra cima deles, FURIA! 💛🖤\n"
        "_#DIADEFURIA #GOFURIA #CS2_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /historia
async def historia(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "💥 HISTÓRIA DA FURIA 💥\n\n"
        "🎮 O COMEÇO DA LENDÁRIA FURIA! 🏆\n"
        "A FURIA nasceu com um objetivo claro: dominar o cenário competitivo! Desde o início, com sua força imbatível e espírito guerreiro, conquistaram as maiores vitórias do CS:GO!\n\n"
        "🔥 Com um time campeão e a torcida mais apaixonada do mundo, FURIA é o símbolo de luta, garra e superação! 🔥\n"
        "_#GoFURIA #RaizDaTorcida #FURIACampeã_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /razao
async def furia_razao(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🔥 POR QUE AMAMOS A FURIA? 🔥\n\n"
        "🖤💛 A FURIA é nossa paixão, é o nosso orgulho!\n"
        "Cada jogada, cada vitória, é um motivo para gritar até perder a voz! 💥💣\n"
        "🏆 Desde o começo, eles provaram que não existem limites!\n"
        "🔥 Juntos, somos mais fortes! 🔥\n"
        "_#FURIA #GoFURIA #UnidosPeloCampeonato_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /recordes
async def furia_recordes(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "💥 RECORDES DA FURIA QUE MARCARAM A HISTÓRIA! 💥\n\n"
        "🏆 A FURIA é uma máquina de quebrar recordes!\n"
        "🔥 Com a nossa torcida em peso, eles conquistam vitórias imbatíveis!\n\n"
        "_#FURIA #Recordes #GoFURIA_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /futuro
async def furia_futuro(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "⚡ O FUTURO DA FURIA É BRILHANTE! ⚡\n\n"
        "🔮 O que vem por aí? Conquistas, vitórias e mais histórias épicas! 🚀\n"
        "💛🖤 O futuro da FURIA é agora! 🖊️💥\n"
        "_#GoFURIA #FuturoDaFURIA #CS2_"
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Comando /time
async def membros(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    membro = random.choice(time_furia)
    legenda = (
        f"🔥 Conheça {membro['nome']} da FURIA! 🔥\n"
        f"Função: {membro['funcao']} \n"
        "_#FURIA #GoFURIA #CS2_"
    )
    await update.message.reply_photo(
        photo=membro["imagem"],
        caption=escapar_markdown_v2(legenda),
        parse_mode='MarkdownV2'
    )

# Comando /torcaconosco
async def torca_conosco(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    mensagem = (
        "🔥 Mostre seu apoio à FURIA! 🔥\n\n"
        "Clique no botão abaixo para fazer uma postagem no X torcendo para o time:\n\n"
        "Torcer no X"
        "https://twitter.com/intent/tweet?text=Vamos+com+tudo%2C+FURIA%21+%F0%9F%92%AA+%23GoFURIA+%23DIADEFURIA+%23CS2 "
    )
    await update.message.reply_markdown_v2(escapar_markdown_v2(mensagem))

# Inicialização do bot
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("proximojogo", proximo_jogo))
    app.add_handler(CommandHandler("historia", historia))
    app.add_handler(CommandHandler("razao", furia_razao))
    app.add_handler(CommandHandler("recordes", furia_recordes))
    app.add_handler(CommandHandler("futuro", furia_futuro))
    app.add_handler(CommandHandler("membros", membros))
    app.add_handler(CommandHandler("torcaconosco", torca_conosco))
    print("✅ Bot rodando... Pressione Ctrl+C para parar.")
    app.run_polling()
