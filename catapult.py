from flask import Flask, request, make_response, render_template
import RPi.GPIO as GPIO
from time import sleep

global fire_motor
global turn_motor

FREQ = 50#hz

app = Flask(__name__, template_folder=".",static_folder="./assets")

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

@app.post("/turn")
def turn():
    global turn_motor
    angle = int(request.json["angle"])
    turn_motor.ChangeDutyCycle(round(360/angle))


@app.post("/fire")
def fire():
    global fire_motor
    fire_motor.ChangeDutyCycle(6)
    sleep(0.5)
    fire_motor.ChangeDutyCycle(2)