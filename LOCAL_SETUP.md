# Локальная настройка и разработка

## Установка зависимостей

```bash
pip install -r requirements.txt
```

## Настройка токена

1. Создайте файл `.env` в корне проекта:
```bash
cp .env.example .env
```

2. Откройте `.env` и добавьте ваш токен:
```env
TELEGRAM_BOT_TOKEN=ВАШ_ТОКЕН_ОТ_BOTFATHER
```

## Запуск бота

```bash
python bot.py
```

## Тестирование

1. Откройте Telegram
2. Найдите своего бота
3. Отправьте команду `/start`
4. Бот должен ответить "канд дурак дурак дурак"

## Остановка бота

Нажмите `Ctrl + C` в терминале

## Режим отладки

Для более подробных логов можно изменить уровень логирования в `bot.py`:

```python
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG  # Измените на DEBUG для более подробных логов
)
```

## Использование виртуального окружения

Рекомендуется использовать виртуальное окружение:

```bash
# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux/Mac)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt

# Запуск бота
python bot.py

# Деактивация
deactivate
```