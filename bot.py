import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import ParseMode
from apis import *
from csv_json import *
from scraping import *
from basededatos import *
import os

# Authentication to manage the bot
TOKEN = os.getenv('TOKEN')

if TOKEN == None:
    print('Lembra indicar a variable TOKEN.')
    print('p. ex.: docker run --rm -e TOKEN=o_teu_token -e API_KEY=a_túa_API_KEY nomebot')
    exit(1)

# Show logs in terminal
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# This function responds to start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="/tempo\n/imaxe\n/joke\n/calendar\n/novas\n/carteleira\n/misterios\n/inferno")

# This function responds to tempo command handler
async def tempo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=api_tempo())

# This function responds to imaxe command handler
async def imaxe(update, context):
    api_imaxe()
    answer = open('imaxedodia.jpg', "rb")
    await context.bot.send_document(chat_id=update.effective_chat.id, document=answer)
    
# This function responds to joke command handler
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=api_joke())

# This function responds to calendar command handler
async def calendar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=api_calendar())

# This function responds to a file handler
async def csv2json(update, context):
    file = await context.bot.get_file(update.message.document)
    filename = update.message.document.file_name
    await file.download_to_drive("files/" + filename)
    tipo = csv_file(filename)
    if tipo == "other":
        await context.bot.send_message(chat_id=update.effective_chat.id, text="No es CSV ni JSON.")
        os.remove("files/" + filename)
    else:
        if type(tipo) == tuple and tipo[0] == "csv2json":
            new_file = f'files/{os.path.splitext(os.path.basename(filename))[0]}.json'
            await context.bot.send_message(chat_id=update.effective_chat.id, text=tipo[1])
        elif tipo == "json2csv":
            new_file = f'files/{os.path.splitext(os.path.basename(filename))[0]}.csv'
        answer = open(new_file, "rb")
        await context.bot.send_document(chat_id=update.effective_chat.id, document=answer)
        os.remove("files/" + filename)
        os.remove(new_file)

# This function responds to novas handler
async def novas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=scraping_novas(), parse_mode=ParseMode.MARKDOWN)

# This function responds to carteleira handler
async def carteleira(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=scraping_carteleira(), parse_mode=ParseMode.MARKDOWN)

# This function responds to misterios handler
async def misterios(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = scraping_misterios()
    if texto:
        await context.bot.send_message(chat_id=update.effective_chat.id, text=texto)

# This function responds to inferno command handler
async def inferno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=basededatos_inferno())

if __name__ == '__main__':
    # Start the application to operate the bot
    application = ApplicationBuilder().token(TOKEN).build()

    # Handler to manage the start command
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    # Handler to manage tempo command
    tempo_handler = CommandHandler('tempo', tempo)
    application.add_handler(tempo_handler)

    # Handler to manage imaxe command
    imaxe_handler = CommandHandler('imaxe', imaxe)
    application.add_handler(imaxe_handler)

    # Handler to manage joke command
    joke_handler = CommandHandler('joke', joke)
    application.add_handler(joke_handler)

    # Handler to manage calendar command
    calendar_handler = CommandHandler('calendar', calendar)
    application.add_handler(calendar_handler)

    # Handler to manage a file
    application.add_handler(MessageHandler(filters.Document.ALL, csv2json))

    # Handler to manage novas command
    novas_handler = CommandHandler('novas', novas)
    application.add_handler(novas_handler)

    # Handler to manage carteleira command
    carteleira_handler = CommandHandler('carteleira', carteleira)
    application.add_handler(carteleira_handler)

    #Handler to manage misterios command
    misterios_handler = CommandHandler('misterios', misterios)
    application.add_handler(misterios_handler)
    
    #Handler to manage inferno command
    inferno_handler = CommandHandler('inferno', inferno)
    application.add_handler(inferno_handler)
    
    # Keeps the application running
    application.run_polling()