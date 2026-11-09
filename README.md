# Bot-Test-Dead

Тестовый Telegram бот, который отвечает на команду /start сообщением "канд дурак дурак дурак".

## 🚀 Установка

1. Склонируйте репозиторий:
```bash
git clone https://github.com/Deadruke/Bot-Test-Dead.git
cd Bot-Test-Dead
```

2. Установите зависимости:
```bash
pip install -r requirements.txt
```

3. Получите токен бота от [@BotFather](https://t.me/BotFather) в Telegram

4. Создайте файл `.env` и добавьте туда токен:
```env
TELEGRAM_BOT_TOKEN=ВАШ_ТОКЕН_ОТ_BOTFATHER
```

5. Запустите бота:
```bash
python bot.py
```

## 📦 Развертывание на Render

Этот проект готов к развертыванию на Render.com.

### Инструкция:

1. Зарегистрируйтесь на [Render.com](https://render.com)

2. Создайте новый Web Service и подключите этот репозиторий

3. Добавьте переменную окружения:
   - **Key**: `TELEGRAM_BOT_TOKEN`
   - **Value**: ваш токен от BotFather

4. Нажмите "Deploy Web Service"

5. После завершения деплоя ваш бот будет доступен по ссылке, которую предоставит Render

### Альтернативный способ (render.yaml):

Если вы используете render.yaml, просто подключите репозиторий к Render и он автоматически определит конфигурацию.

## 📝 Команды

- `/start` - бот отвечает "канд дурак дурак дурак"

## 🛠️ Технологии

- Python 3.8+
- python-telegram-bot 20.7
- Render (для деплоя)

## 📄 Лицензия

MIT