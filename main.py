from gpiozero import MotionSensor
import cv2
import telebot
import time


def TelegramSendFile(input_file):
    # Написать код отправки файла в Телеграмм: Матяж Владимир
    pass


def main():
    path = "images/"
    pir = MotionSensor(4)
    try:
        camera = cv2.VideoCapture(0)
        while True:
            #
            current_Time = str(time.strftime("%Y%m%d-%H%M%S"))

            print("Motion detected! ", current_Time)
            if not camera.isOpened():
                camera.open(0)

            result, image = camera.read()
            cv2.imwrite(path+current_Time+'.jpg', image)
            camera.release()

    except Exception as e:
        print("Some error. ", e)


if __name__ == "__main__":
    main()
