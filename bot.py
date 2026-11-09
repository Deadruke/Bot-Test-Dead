import logging
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
    # Замените YOUR_BOT_TOKEN на ваш токен бота
    TOKEN = 'YOUR_BOT_TOKEN'
    
    # Создаем приложение
    app = ApplicationBuilder().token(TOKEN).build()
    
    # Добавляем обработчик команды /start
    app.add_handler(CommandHandler("start", start))
    
    # Запускаем бота
    logger.info("Бот запущен")
    app.run_polling()

if __name__ == '__main__':
    main()