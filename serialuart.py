import pygame
import serial, math, time
pygame.init()

testStandAlone = False;

if  testStandAlone :
    uart = serial.Serial('COM4', 19200, timeout=1)
    uartinput = b'\x00'
else :
    uart = serial.Serial('COM3', 19200, timeout=0.0167)
    uartinput = b'\x00'

leftFlipperuart = False
rightFlipperuart = False

def listen():
    global uartinput
    if testStandAlone :
        uart.flushInput()
        time.sleep(0.2)
        if uart.in_waiting > 0 :
            uartinput = uart.read()
        print(uartinput)
    else :
        uart.flushInput()
        time.sleep(0.008)
        uartinput = uart.read()
    global leftFlipperuart
    global rightFlipperuart
    rightuartinput = uartinput[0] & 15
    leftuartinput = (uartinput[0] >> 4) & 15
    print([leftuartinput,rightuartinput])
    if rightuartinput>0 :
        rightFlipperuart = True
    else :
        rightFlipperuart = False
    if leftuartinput > 0 :
        leftFlipperuart = True
    else :
        leftFlipperuart = False
    return [(5*math.pi/36)-(leftuartinput*(math.pi/54)),(31*math.pi/36)+(rightuartinput*(math.pi/54))]


def leftFlipper():
    return leftFlipperuart
    

def rightFlipper():
    return rightFlipperuart