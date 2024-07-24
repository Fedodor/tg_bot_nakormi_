![Workflow badge](https://github.com/Fedodor/tg_bot_nakormi/nakormi/actions/workflows/main.yml/badge.svg)

# Телеграм бот проекта помощи домашним животным Накорми 🐈

Здесь будет описание бота
***
### Установка
- Создайте бота через [@BotFather](https://t.me/botfather) по [инструкции](https://core.telegram.org/bots/tutorial#obtain-your-bot-token).
- Добавьте описание и команды для своего бота из файла [bot_texts.txt](https://github.com/Fedodor/tg_bot_nakormi/nakormi/blob/main/bot_texts.txt).
- Клонируйте проект:
```
git clone git@github.com:Fedodor/tg_bot_nakormi/nakormi.git
``` 
- Перейдите в директорию nakormi:
```
cd beck_inventory_telegram_bot
``` 
- Cоздайте переменные окружения по [образцу](https://github.com/Fedodor/tg_bot_nakormi/nakormi/blob/main/.env.example).
- Запустите Docker-compose:
```
docker compose -f docker-compose-dev.yml up
``` 
Готово! 📝 