import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "ВСТАВ_СЮДИ_TOKEN_ВІД_BOTFATHER"
ADMIN_CHAT_ID = 8514615115  # ВСТАВ СВІЙ chat_id

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# --- START ---
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🛋 Замовити перетяжку")
    kb.add("💰 Ціни", "📞 Контакти")

    await message.answer(
        "👋 Вітаємо!\n\n"
        "Ми займаємось ТІЛЬКИ перетяжкою меблів:\n"
        "🛋 Дивани\n🪑 Кріслa\n🛏 Ліжка\n\n"
        "📸 Працюємо по фото\n"
        "🚚 Виїзд майстра — 500 грн\n\n"
        "Оберіть дію 👇",
        reply_markup=kb
    )

# --- ЦІНИ ---
@dp.message_handler(lambda m: m.text == "💰 Ціни")
async def prices(message: types.Message):
    await message.answer(
        "💰 Орієнтовні ціни:\n\n"
        "🪑 Крісло — від 2500 грн\n"
        "🛋 Диван — від 6000 грн\n"
        "🛋 Кутовий диван — від 8500 грн\n"
        "🛏 Ліжко — від 4000 грн\n\n"
        "⚠️ Точна ціна — після фото"
    )

# --- КОНТАКТИ ---
@dp.message_handler(lambda m: m.text == "📞 Контакти")
async def contacts(message: types.Message):
    await message.answer(
        "📞 Телефон: +38 099 666 06 71\n"
        "📩 Напишіть у бот — відповімо швидко"
    )

# --- ЗАМОВЛЕННЯ ---
@dp.message_handler(lambda m: m.text == "🛋 Замовити перетяжку")
async def order(message: types.Message):
    await message.answer(
        "✍️ Напишіть одним повідомленням:\n\n"
        "1️⃣ Місто / район\n"
        "2️⃣ Тип меблів\n"
        "3️⃣ Приблизні розміри\n"
        "4️⃣ Коли зручно\n\n"
        "📸 Після цього надішліть фото меблів"
    )

# --- ПРИЙОМ ТЕКСТУ ---
@dp.message_handler(content_types=types.ContentType.TEXT)
async def get_text(message: types.Message):
    await bot.send_message(
        ADMIN_CHAT_ID,
        f"🛋 НОВА ЗАЯВКА\n\n"
        f"👤 @{message.from_user.username}\n"
        f"📝 {message.text}"
    )

# --- ПРИЙОМ ФОТО ---
@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo(message: types.Message):
    await bot.send_photo(
        ADMIN_CHAT_ID,
        message.photo[-1].file_id,
        caption=f"📸 Фото від @{message.from_user.username}"
    )

    await message.answer("✅ Дякуємо! Майстер скоро з вами звʼяжеться.")

# --- RUN ---
if name == "__main__":
    executor.start_polling(dp, skip_updates=True)
    pipinstallaiogram
    