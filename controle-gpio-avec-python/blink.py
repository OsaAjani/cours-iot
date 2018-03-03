#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

LED = 7

def turn_high (gpio) :
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, GPIO.HIGH)

def turn_low (gpio) :
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, GPIO.LOW)


while True :
    turn_high(LED)
    time.sleep(2)
    turn_low(LED)
    time.sleep(2)
