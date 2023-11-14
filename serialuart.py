import pygame
import serial
pygame.init()

uart = serial.Serial('COM3', 19200, timeout=1)

leftFlipperuart = False
rightFlipperuart = False

def listen():
    #uartinput = 0xF0
    global leftFlipperuart
    global rightFlipperuart
    uartinput = uart.read()
    if uartinput == 0x00 :
        leftFlipperuart = False
        rightFlipperuart = False
    elif uartinput == 0x0F :
        leftFlipperuart = False
        rightFlipperuart = True
    elif uartinput == 0xF0 :
        leftFlipperuart = True
        rightFlipperuart = False
    elif uartinput == 0xFF :
        leftFlipperuart = True
        rightFlipperuart = True


def leftFlipper():
    return leftFlipperuart
    

def rightFlipper():
    return rightFlipperuart