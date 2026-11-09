import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Функция обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработка команды /start"""
    user = update.effective_user
    await update.message.reply_text('канд дурак дурак дурак')
    logger.info(f"Команда /start от пользователя {user.full_name} (ID: {user.id})")

def main():
    """Запуск бота"""
    # Получаем токен из переменных окружения
    token = os.environ.get('BOT_TOKEN')
    
    if not token:
        logger.error("BOT_TOKEN не найден в переменных окружения!")
        logger.error("Пожалуйста, добавьте BOT_TOKEN в Render как переменную окружения")
        return
    
    # Создаем приложение (в новой версии библиотеки это возвращает Application, а не Updater)
    app = ApplicationBuilder().token(token).build()
    
    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    logger.info("Бот запущен")
    app.run_polling()

if __name__ == '__main__':
    main()