import cv2
import serial
from Utils.utils import ImaginaryBox, CascadeClassifier, Video, Color, Arduino, SerialCommunication
# import threading
# from Voice.Voice import run_conversation

FACE_CASCADE = cv2.CascadeClassifier(CascadeClassifier.FRONT_FACE.value)
SERIAL_COMMUNICATION = serial.Serial(port=Arduino.PORT.value, baudrate=Arduino.BAUD_RATE.value, write_timeout=1)

capture = cv2.VideoCapture(Video.CAMERA.value)

while True:

    src, image = capture.read()

    flipped_image = cv2.flip(image, 1)
    gray_image = cv2.cvtColor(flipped_image, cv2.COLOR_BGR2GRAY)

    cv2.rectangle(flipped_image, (ImaginaryBox.X_COORDINATE.value, ImaginaryBox.Y_COORDINATE.value),
                  (ImaginaryBox.X_COORDINATE.value + ImaginaryBox.WIDTH.value,
                   ImaginaryBox.Y_COORDINATE.value + ImaginaryBox.HEIGHT.value), Color.RED.value, 2)

    faces = FACE_CASCADE.detectMultiScale(gray_image, 1.1, 4)

    for (x, y, width, height) in faces:

        cv2.rectangle(flipped_image, (x, y), (x + width, y + height), Color.BLUE.value, 2)

        x1, y1, width1, height1 = int(x), int(y), int(width), int(height)

        circle_x = x1 + int((width1 / 2))
        circle_y = y1 + int((height1 / 2))

        cv2.circle(flipped_image, (circle_x, circle_y), 2, Color.GREEN.value, -1)

        if width1 > Video.FACE_TRACKING_WIDTH.value:

            if circle_x < (ImaginaryBox.X_COORDINATE.value + 60):
                SERIAL_COMMUNICATION.write(SerialCommunication.LEFT.value.encode())
                cv2.putText(flipped_image, f'LEFT {SerialCommunication.LEFT.value}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            Color.GREEN.value, 2)
                print('left', SerialCommunication.LEFT.value)
                break

            if circle_x > (ImaginaryBox.X_COORDINATE.value + 120):
                SERIAL_COMMUNICATION.write(SerialCommunication.RIGHT.value.encode())
                cv2.putText(flipped_image, f'RIGHT {SerialCommunication.RIGHT.value}', (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1, Color.GREEN.value, 2)
                print("right", SerialCommunication.RIGHT.value)
                break

            if circle_y < (ImaginaryBox.Y_COORDINATE.value + 60):
                SERIAL_COMMUNICATION.write(SerialCommunication.UP.value.encode())
                cv2.putText(flipped_image, f'UP {SerialCommunication.UP.value}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1, Color.GREEN.value, 2)
                print("up", SerialCommunication.UP.value)
                break

            if circle_y > (ImaginaryBox.Y_COORDINATE.value + 120):
                SERIAL_COMMUNICATION.write(SerialCommunication.DOWN.value.encode())
                cv2.putText(flipped_image, f'DOWN {SerialCommunication.DOWN.value}', (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1, Color.GREEN.value, 2)
                print("down", SerialCommunication.DOWN.value)
                break

            if ((circle_x > (ImaginaryBox.X_COORDINATE.value + 60)) and
                (circle_x < (ImaginaryBox.X_COORDINATE.value + 120))) and \
                    ((circle_y > (ImaginaryBox.Y_COORDINATE.value + 60)) and
                     (circle_y < (ImaginaryBox.Y_COORDINATE.value + 120))):
                cv2.rectangle(flipped_image, (x, y), (x + width, y + height), Color.GREEN.value, 2)

                cv2.putText(flipped_image, 'Face Tracked', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            Color.GREEN.value, 2)
                cv2.putText(flipped_image, f'FACE TRACKED', (30, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            Color.GREEN.value, 2)
                # threading.Thread(target=run_conversation).start()

                # SERIAL_COMMUNICATION.write(SerialCommunication.FACE_DETECTED.value.encode())
                # print(SERIAL_COMMUNICATION.readline())
    cv2.imshow('img', flipped_image)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

capture.release()
