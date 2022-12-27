# Интернет вещей

## Состав группы
### КС-20-1б
1. Камянецький Сергей `Kam-Sergei`
2. Морохин Александр `AlexandrFiner`
3. Матяж Владимир `79824`

## Описание программы
К плате Raspberry pi подключаются, используя пины, датчик движения и камера, используя USB порт. Если датчик движения отдает сигнал, то делается фотография и отправляется в телеграмм бот.

------

# Установка
1. Установите менеджер пакетов `apt-get install python3-pip`
2. Установите дополнительные инструменты `sudo apt install -y build-essential libssl-dev libffi-dev python3-dev`
3. Установите venv `sudo apt install -y python3-venv`
4. Создайте виртуальное окружение `python3 -m venv env`
5. Активируйте виртуальную среду `source env/bin/activate`
6. Выполните установку пакетов из файла requirements.txt `pip install -r requirements.txt`
7. Скопировать конфиг и установить токен Telegram `cp config.example.py config.py`
