import OPi.GPIO as GPIO
import cv2
import telebot
import time
from threading import Thread
from config import token

user_list = []

bot = telebot.TeleBot(token, parse_mode=None)


@bot.message_handler(commands=['start'])
def add_to_list(message):
    if message.chat.id not in user_list:
        bot.reply_to(message, "Теперь вы будете получать изображения")
        user_list.append(message.chat.id)
    else:
        bot.reply_to(message, "!! Вы уже получаете уведомления")


@bot.message_handler(commands=['stop'])
def add_to_list(message):
    if message.chat.id in user_list:
        bot.reply_to(message, "Вы отключились от уведомлений")
        user_list.remove(message.chat.id)
    else:
        bot.reply_to(message, "!! Вы еще не получаете уведомления")


def TelegramSendFile(input_file):
    for chatId in user_list:
        bot.send_photo(chatId, open(input_file, 'rb'))


def main():
    path = "images/"
    PORT = 5
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PORT, GPIO.OUT)
    GPIO.output(PORT, GPIO.HIGH)

    camera = cv2.VideoCapture(1)
    while True:
        current_Time = str(time.strftime("%Y%m%d-%H%M%S"))

        print("Motion detected! ", current_Time)
        if not camera.isOpened():
            camera.open(0)

        result, image = camera.read()
        cv2.imwrite(f"{path}image.jpg", image)
        TelegramSendFile(f"{path}image.jpg")

        GPIO.OUTPUT(PORT, GPIO.LOW)
        time.sleep(5)
        GPIO.output(PORT, GPIO.HIGH)


if __name__ == "__main__":
    threadBot = Thread(target=bot.polling)
    threadCamera = Thread(target=main)
    threadBot.start()
    threadCamera.start()
    threadBot.join()
    threadCamera.join()
