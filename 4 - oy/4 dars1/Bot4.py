from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

CARS_INFO = {
    "Tesla Model S": {
        "description": "Tesla Model S - elektr avtomobil. Yuqori tezlik va katta masofa.",
        "image_url": "c:\Users\user\Pictures\O'zim\The weeknd\2021_Tesla_Model_S_P2_Long_Range_front_right_view.jpg"  
    },
    "BMW X5": {
        "description": "BMW X5 - hashamatli SUV, katta quvvat va qulaylik.",
        "image_url": "c:\Users\user\Pictures\O'zim\The weeknd\585d8660-215c-4396-95a9-267473baa569_2018+BMW+X5+Front+3_4+Driving+1.jpg"
    },
    "Audi A8": {
        "description": "Audi A8 - zamonaviy texnologiyalar va qulaylik bilan jihozlangan.",
        "image_url": "c:\Users\user\Pictures\O'zim\The weeknd\04477c50108a299204c7cc593a0ddec9.jpeg"
    },
    "Mercedes-Benz G-Class": {
        "description": "Mercedes-Benz G-Class - yuqori darajadagi qudrat va mustahkamlik.",
        "image_url": "c:\Users\user\Pictures\O'zim\The weeknd\images.jpeg"
    },
    "Ford Mustang": {
        "description": "Ford Mustang - sport avtomobil, tezlik va klassik dizaynning uygunligi.",
        "image_url": "c:\Users\user\Pictures\O'zim\The weeknd\1200px-2018_Ford_Mustang_GT_5.0.jpg"
    }
}

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Tesla Model S", callback_data='Tesla Model S')],
        [InlineKeyboardButton("BMW X5", callback_data='BMW X5')],
        [InlineKeyboardButton("Audi A8", callback_data='Audi A8')],
        [InlineKeyboardButton("Mercedes-Benz G-Class", callback_data='Mercedes-Benz G-Class')],
        [InlineKeyboardButton("Ford Mustang", callback_data='Ford Mustang')]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Avtomobilni tanlang:", reply_markup=reply_markup)

async def show_car_info(update: Update, context):
    query = update.callback_query
    await query.answer()

    car_name = query.data
    logger.info(f'Car name selected: {car_name}')  

    car_info = CARS_INFO.get(car_name, None)
    if car_info:
        logger.info(f'Car info found: {car_info}') 
        description = car_info["description"]
        image_url = car_info["image_url"]

        await query.message.reply_photo(photo=image_url, caption=f"{car_name}\n\n{description}")

        back_keyboard = [[InlineKeyboardButton("Ortga", callback_data='back')]]
        reply_markup = InlineKeyboardMarkup(back_keyboard)
        await query.message.reply_text("Ortga qaytish uchun bosishingiz mumkin:", reply_markup=reply_markup)
    else:
        logger.warning(f'No info found for {car_name}')  

async def go_back(update: Update, context):
    query = update.callback_query
    await query.answer()

    if query.data == 'back':
        await start(update, context)

async def main():
    application = ApplicationBuilder().token("8154458815:AAGRlIxDQmCPNXbgTZMpd7W85Q-GJleEF6Y").build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(CallbackQueryHandler(show_car_info, pattern="^(Tesla Model S|BMW X5|Audi A8|Mercedes-Benz G-Class|Ford Mustang)$"))

    application.add_handler(CallbackQueryHandler(go_back, pattern='back'))
 
    await application.start_polling()

import asyncio
asyncio.run(main())
