from gpiozero import LED, MotionSensor
import cv2
import telebot
import time
from threading import Thread

user_list = []

token = '5814884989:AAGzD3cRDpIc1bJhKMBFMuLSOmRPRSVSTKU'
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
    # Написать код отправки файла в Телеграмм: Матяж Владимир
    for chatId in user_list:
        bot.send_photo(chatId, open(input_file, 'rb'))


def main():
    path = "images/"
    pir = MotionSensor(4)
    led = LED(17)
    
    try:
        camera = cv2.VideoCapture(0)
        while True:
            pir.when_motion
            led.blink()
            current_Time = str(time.strftime("%Y%m%d-%H%M%S"))

            print("Motion detected! ", current_Time)
            if not camera.isOpened():
                camera.open(0)

            result, image = camera.read()
            image_path = path + 'image' + '.jpg'
            cv2.imwrite(image_path, image)
            TelegramSendFile(image_path)
            camera.release()
            pir.when_no_motion

    except Exception as e:
        print("Some error. ", e)


if __name__ == "__main__":
    threadBot = Thread(target=bot.polling)
    threadCamera = Thread(target=main)
    threadBot.start()
    threadCamera.start()
    threadBot.join()
    threadCamera.join()
