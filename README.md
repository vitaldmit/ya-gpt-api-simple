# API для исправления текста с помощью YandexGPT

Простейшее Python-приложение, использующее модель [YandexGPT Lite](https://yandex.cloud/ru/docs/foundation-models/quickstart/yandexgpt) через API Yandex Cloud для исправления текста. Но можно настроить для использования любой другой модели и задачи.

## Возможности

- Обнаружение и исправление ошибок в тексте
- Использование модели YandexGPT Lite
- Простая интеграция с API
- Поддержка потоковой передачи (настраиваемая)

## Требования

- Python 3.9+
- Аккаунт Yandex Cloud
- IAM токен
- ID папки из Yandex Cloud

## Установка

1. Настройте виртуальное окружение:
```sh
python -m venv ya-gpt-api-simple
cd ya-gpt-api-simple
source bin/activate
mkdir src; cd src
```

2. Клонируйте репозиторий
```sh
git clone https://github.com/vitaldmit/ya-gpt-api-simple.git .
```

3. Установите зависимости
```sh
pip install -r requirements.txt
```

## Настройка

Создайте файл `secret.py` с помощью команды `mv secret.simple secret.py` с вашими учетными данными:

```
IAM_TOKEN = "ваш_iam_токен"
FOLDER_ID = "ваш_id_папки"
```

## Использование

Запустите приложение с помощью команды:
```sh
python main.py
```
