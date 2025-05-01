# 🐗 FURIA Bot - Telegram Edition

**FURIA Bot** é o seu companheiro de torcida, direto no Telegram! Desenvolvido em Python, ele entrega informações sobre o time de CS:GO da FURIA com estilo, paixão e muita dedicação pela camisa! 🖤💛

---

## 📌 Objetivo

Criar um bot de Telegram para fãs da FURIA e entusiastas de CS:GO, com foco no time profissional da organização. A ideia é ter um "amigo virtual" que saiba de todos os jogos, recordes e história da equipe.

> 💡 *Futuramente planejamos atualizações automáticas e integração com o Discord!*

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **python-telegram-bot** – interação com a API do Telegram
- **python-dotenv** – leitura de variáveis sensíveis

---

## 🛠️ Instalação e Execução

### Pré-requisitos

- Python 3.7+
- Conta no Telegram
- Bot criado via [@BotFather](https://core.telegram.org/bots#botfather)

### Passo a passo

```bash
# Clone o repositório
git clone https://github.com/Frank1br/furiabot.git
cd furiabot

# Crie o arquivo .env
echo TELEGRAM_TOKEN=seu_token_aqui > .env

# Instale as dependências
pip install -r requirements.txt

# Execute o bot
python main.py
```

---

## 🔐 Configuração

Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave de API do Telegram:

```
TELEGRAM_TOKEN=seu_token_aqui
```

---

## 🗂️ Estrutura do Projeto

```plaintext
├── main.py            # Arquivo principal do bot
├── .env               # Token do Telegram
├── requirements.txt   # Dependências
└── README.md          # Documentação furiosa
```

---

## 💬 Comandos disponíveis

- `/start` – Inicia a conversa com o bot
- `/proximojogo` – Mostra o próximo jogo da FURIA
- `/historia` – Conta a história da FURIA
- `/razao` – Por que amamos a FURIA
- `/recordes` – Recordes da FURIA
- `/futuro` – O futuro da FURIA
- `/membros` – Conheça nosso time de maneira aleatória 🖤🔥
- `/torcaconosco` – Poste torcendo pela FURIA

---

## 🧪 Testes

Atualmente, este projeto **não possui testes automatizados**. Mas contribuições são bem-vindas para isso também!

---

## 🤝 Contribuindo

Contribuições são super bem-vindas! Para colaborar:

1. Faça um fork
2. Crie uma branch: `git checkout -b feat/sua-feature`
3. Siga o padrão de commits: `feat`, `fix`, `refactor`, etc.
4. Abra um Pull Request

Se encontrar uma issue, sinta-se à vontade para abrir um PR corrigindo-a! 🛠️

---

## 📄 Licença

Este projeto **ainda não possui uma licença definida**. Use com sabedoria e respeito à comunidade.

---

## 👤 Autor

- Nome: **Frank Oliveira**
- Nickname: **Frank1br**
- GitHub: [github.com/Frank1br](https://github.com/Frank1br)

---

## 🐗 FURIA acima de tudo!

_"Não é só um jogo. É o sentimento de vestir preto e dourado em cada round."_  
#GoFURIA #FURIAcs #TelegramBot