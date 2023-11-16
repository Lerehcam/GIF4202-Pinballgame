import pygame
import serial
pygame.init()

uart = serial.Serial('COM3', 19200, timeout=1)

leftFlipperuart = False
rightFlipperuart = False

def listen():
    #uartinput = 0x0F
    global leftFlipperuart
    global rightFlipperuart
    uart.flushInput()
    uartinput = uart.read()
    print(uartinput)
    if uartinput == b'\x00' :
        leftFlipperuart = False
        rightFlipperuart = False
    elif uartinput == b'\x0f' :
        leftFlipperuart = False
        rightFlipperuart = True
    elif uartinput == b'\xf0' :
        leftFlipperuart = True
        rightFlipperuart = False
    elif uartinput == b'\xff' :
        leftFlipperuart = True
        rightFlipperuart = True


def leftFlipper():
    return leftFlipperuart
    

def rightFlipper():
    return rightFlipperuart