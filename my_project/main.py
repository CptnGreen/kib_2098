#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

# создаём объекты класса Motor
# для управления реальными моторами

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# для подачи тока на моторы (от -100 до 100)
# используем метод dc объектов класса Motor

# крутиться вправо 1 секунду:

left_motor.dc(50)
right_motor.dc(-50)
wait(1000)

# сочиняем функцию для поворота налево:

def kib_turn_left():
    left_motor.dc(50)
    right_motor.dc(-50)
    wait(1000)
    left_motor.dc(0)
    right_motor.dc(0)

# вызываем её на исполнение:

kib_turn_left()
    
# функция для поворота робота на 
# произвольный неотрицательный угол 
# (k - отладочный коэффициент):

def kib_turn(angle):
    k = 10
    left_motor.dc(50)
    right_motor.dc(-50)
    wait(k * angle)
    left_motor.dc(0)
    right_motor.dc(0)

kib_turn_left(360)
kib_turn_left(720)
kib_turn_left(90)


    