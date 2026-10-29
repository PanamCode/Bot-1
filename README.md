# 📝 Lead Collection Bot

Чистый Telegram-бот для сбора заявок с сохранением в Google Sheets и уведомлением администратору.

**Стек:** aiogram 3 • gspread • Bothost

## Возможности

- Приветствие и главное меню
- Пошаговая форма (Имя → Телефон → Комментарий)
- Сохранение заявок в Google Таблицу
- Мгновенное уведомление в личку администратору
- Возможность отмены на любом этапе

## Быстрый старт (локально)

1. Клонируй репозиторий
2. Создай `.env` на основе `.env.example`
3. Добавь `credentials/service_account.json` (Google Service Account)
4. 
```bash
pip install -r requirements.txt
python -m bot.main
```

## Настройка Google Sheets

1. Создай проект в Google Cloud Console
2. Включи **Google Sheets API** и **Google Drive API**
3. Создай Service Account → скачай JSON-ключ
4. Создай Google Таблицу и дай доступ сервисному аккаунту (как Редактор)
5. Скопируй ID таблицы из URL

## Деплой на Bothost

1. Подключи репозиторий на [bothost.ru](https://bothost.ru)
2. Добавь переменные окружения:
   - `BOT_TOKEN`
   - `ADMIN_ID`
   - `SPREADSHEET_ID`
3. Загрузи `service_account.json` в папку `credentials/` через файловый менеджер
4. Команда запуска: `python -m bot.main`

## Структура проекта

```
bot/
├── main.py
├── config.py
├── states.py
├── handlers/
├── keyboards/
└── services/
```
