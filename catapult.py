from flask import Flask, request, make_response, render_template
import RPi.GPIO as GPIO
from time import sleep
from sys import exit

global fire_motor
global turn_motor
global currentDutyCycle
FREQ = 50#hz

app = Flask(__name__, template_folder=".",static_folder=".")

app.get("/setup")
def setup():
    global fire_motor
    global turn_motor
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(13,GPIO.OUT)
    fire_motor = GPIO.PWM(11,FREQ)
    turn_motor = GPIO.PWM(13,FREQ)
    fire_motor.start(0)
    turn_motor.start(0)

app.get("/shutdown")
def shutdown():
    global fire_motor
    global turn_motor
    fire_motor.stop()
    turn_motor.stop()
    GPIO.cleanup()
    exit()

@app.post("/left")
def turn_left():
    global turn_motor
    global currentDutyCycle
    if currentDutyCycle < 12:
        currentDutyCycle += 1
    turn_motor.ChangeDutyCycle(currentDutyCycle)


@app.post("/right")
def turn_right():
    global turn_motor
    global currentDutyCycle
    if currentDutyCycle > 2:
        currentDutyCycle -= 1
    turn_motor.ChangeDutyCycle(currentDutyCycle)

@app.post("/fire")
def fire():
    global fire_motor
    fire_motor.ChangeDutyCycle(6)
    sleep(0.5)
    fire_motor.ChangeDutyCycle(2)

app.get("/")
def main():
    return render_template("index.html")