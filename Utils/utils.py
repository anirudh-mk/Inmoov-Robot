from enum import Enum


class ImaginaryBox(Enum):
    X_COORDINATE = 230
    Y_COORDINATE = 150
    WIDTH = 180
    HEIGHT = 180


class CascadeClassifier(Enum):
    FRONT_FACE = 'haarcascade_frontalface_default.xml'


class Video(Enum):
    CAMERA = 0
    FACE_TRACKING_WIDTH = 150


class Color(Enum):
    RED = (0, 0, 255)
    BLUE = (255, 0, 0)
    GREEN = (0, 255, 0)


class SerialCommunication(Enum):
    LEFT = 'A'
    RIGHT = 'D'
    UP = 'W'
    DOWN = 'S'
    FACE_DETECTED = 'Y'


class Arduino(Enum):
    PORT = 'COM3'
    BAUD_RATE = 9600
