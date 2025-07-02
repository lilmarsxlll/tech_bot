import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

if not API_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Клавиатура с кнопками FAQ и Контакты
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='FAQ')],
        [KeyboardButton(text='Контакты')]
    ],
    resize_keyboard=True
)


faq_data = {
    "<b>Какие сервисы мы предлагаем?</b>": "Мы предлагаем ряд услуг, которые помогают бизнесу процветать. Они включают разработку AI-решений под ключ, платформы и инструменты для работы с данными и AI, специализированные AI-услуги, аналитика данных и консалтинг, исследования и разработка, оптимизация бизнес-процессов/",
     "<b>Какая экспертиза у нашей компании?</b>": "У нас есть техническая экспертиза с Core AI/ML: машинное обучение (ML), глубокое обучение (DL), обработка данных, математика и статистика, MLOps. Экспертиза в специализированных доменах AI: компьютерное зрение, обработка естественного языка (NLP), рекомендательные системы, предиктивная аналитика и голосовые технологии. Мы всегда в списке гостей на таких мероприятиях как ods.ai и DataFest.",
     "<b>Кто наши клиенты?</b>": "Финансы: Кредитный скоринг, фрод-детекция, алготрейдинг, риск-менеджмент. Ритейл и E-commerce: Управление ассортиментом, прогнозирование спроса, персонализация, оптимизация логистики. Здравоохранение и медицина: Анализ медицинских изображений, помощь в диагностике, разработка лекарств, обработка медицинских записей. Промышленность и строительство: Предиктивное обслуживание (PdM), контроль качества, оптимизация производства, цифровые двойники и цифровое зрение. Телеком: Прогнозирование оттока абонентов, оптимизация сетей, анализ клиентского опыта. Маркетинг и Реклама: Таргетирование, оптимизация кампаний, анализ эффективности каналов.",
     "<b>Как мне стать вашим клиентом или стратегическим партнером?</b>": "Стать нашим клиентом очень просто! Начните с того, что свяжитесь с нами через наш сайт или напрямую с нашей командой, чтобы назначить бесплатную первичную консультацию. Во время этой встречи мы обсудим цели вашего бизнеса, проблемы и области, в которых вам нужна поддержка."


}

@dp.message(Command(commands=["start", "help"]))
async def send_welcome(message: Message):
    await message.answer("Привет! Я бот AI Tech. Выберите интересующую вас опцию:", reply_markup=keyboard)

@dp.message(lambda msg: msg.text and msg.text.lower() == 'faq')
async def faq_handler(message: Message):
    full_faq_text = ""
    for question, answer in faq_data.items():
        full_faq_text += f"❓ {question}\n\n{answer}\n\n"
    await message.answer(full_faq_text.strip(), parse_mode='HTML')

@dp.message(lambda msg: msg.text == 'Контакты')
async def contacts_handler(message: Message):
    await message.answer("Связаться с нами можно по ссылке: https://t.me/ai_tech_llc")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
