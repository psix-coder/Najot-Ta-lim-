# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# mashinalr = {
#     "Tesla Model S": {
#         "info": "Tesla Model S - bu elektrokuch bilan yuruvchi sport avtomobil.",
#         "image_url": "https://tesla-cdn.thron.com/delivery/public/image/tesla/xyz.jpg"
#     },

#     "BMW X5": {
#         "info": "BMW X5 - bu yuqori sifatli nemis SUV avtomobil.",
#         "image_url": "https://example.com/bmw_x5.jpg"
#     },
#     "Audi A6": {
#         "info": "Audi A6 - nemis brendining yuqori darajali biznes sedan avtomobili.",
#         "image_url": "https://example.com/audi_a6.jpg"
#     },
#     "Toyota Camry": {
#         "info": "Toyota Camry - bu yuqori sifatli va ishonchli sedan avtomobil.",
#         "image_url": "https://example.com/toyota_camry.jpg"
#     },
#     "Mercedes-Benz E-Class": {
#         "info": "Mercedes-Benz E-Class - bu biznes darajasidagi hashamatli sedan.",
#         "image_url": "https://example.com/mercedes_e_class.jpg"
#     }
# }

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     keyboard = [
#         [InlineKeyboardButton(car, callback_data=car)] for car in mashinalr.keys()
#     ]
#     qaytar = InlineKeyboardMarkup(keyboard)
#     await update.message.reply.text('Avtomabilni tanlang:'),qaytar = qaytar

