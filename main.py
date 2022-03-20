import requests
import pynmcli
import pexpect
import re
from flask import Flask, render_template, request, jsonify
import socket
import sys
from Naked.toolshed.shell import muterun_js
import json
from flask_cors import CORS
import ipaddress
import sys
import keyboard
import RPi.GPIO as GPIO
import board
import neopixel
import os
import subprocess
# from pynput.keyboard import Controller, Key
# pkeyboard = Controller()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
# to write aplhanumeric use keyboard.write("A")
# to use enter backspace space use keyboard.send("value") where send = press + release
# host_name = IPAddr
counter = 1
state = 0
pin1 = board.D18
pixels = neopixel.NeoPixel(pin1, 150, brightness = 1.0)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

@app.route("/connect_wifi", methods=[ 'POST'])
def connect_wifi():
    data = request.json
    print(data)
    result = pynmcli.get_data(pynmcli.NetworkManager.Device().wifi().connect(data["wifi"] +" password " + data["pass"]).execute())
    return result

@app.route("/scan_wifi")
def scan_wifi():
    result = pynmcli.get_data(pynmcli.NetworkManager.Device().wifi().execute())
    return jsonify(result)

@app.route("/checkcon")
def checkcon():
    vSSID = subprocess.check_output("nmcli con show Home | grep '802-11-wireless.ssid' | awk '{print $2}'", shell=True, encoding="utf-8").strip()
    vSTATE = subprocess.check_output("nmcli con show Home | grep 'GENERAL.STATE' | awk '{print $2}'", shell=True, encoding="utf-8").strip()
    vIP = subprocess.check_output("nmcli con show Home | grep 'IP4.ADDRESS' | awk '{print $2}'", shell=True, encoding="utf-8").strip()
    print (vSTATE)
    print (vSSID)
    print (vIP)
    if(vSTATE == "activated"):
        return (vSSID)
    else:
        return "Not Connected"





@app.route("/")
def main():
    # Pass the template data into the template main.html and return it to the user
    print("Home Called")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "Home"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("auth response Sent")
    return response

@app.route("/auth/<action>")
def action_auth(action):
    print("auth Called")
    data = {}
    data["Name"] = "skorboard"
    data["Service"] = socket.gethostname()
    if action == "get":
        data["Status"] = "Enabled"
    if action == "set":
        data["Status"] = "Disabled"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("auth response Sent")
    return response
@app.route("/api/v1/ok")
def action_ok():
    print("Enter Called")
    keyboard.send("enter")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "Ok"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("Ok response Sent")
    return response

@app.route("/api/v1/back")
def backspace():
    print("backspace Called")
    keyboard.send("backspace")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "backspace"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("backspace response Sent")
    return response

@app.route("/api/v1/exit")
def exit():
    print("exit Called")
    keyboard.send("esc")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "exit"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("exit response Sent")
    return response

@app.route("/api/v1/space")
def space():
    print("space Called")
    keyboard.send("space")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "space"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("space response Sent")
    return response

@app.route("/api/v1/btnLeft")
def action_left():
    print("btnLeft arrow Called")
    keyboard.send("left")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnLeft arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnLeft arrow response Sent")
    return response

@app.route("/api/v1/btnRight")
def btnRight():
    print("btnRight arrow Called")
    keyboard.send("right")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnRight arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnRight arrow response Sent")
    return response

@app.route("/api/v1/btnUp")
def btnUp():
    print("btnUp arrow Called")
    keyboard.send("up")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnUp arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnUp arrow response Sent")
    return response

@app.route("/api/v1/btnDown")
def btnDown():
    print("btnDown arrow Called")
    keyboard.send("down")
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "btnDown arrow"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("btnDown arrow response Sent")
    return response

@app.route("/api/v1/ledoff",methods=["OPTIONS", "GET"])
def ledoff():
    print("Led off Called")
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18, GPIO.OUT)
    pixels = neopixel.NeoPixel(board.D18, 150, brightness = 1.0)
    pixels.fill((0, 0, 0))

    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "led response"
    data["status"] = "1"
    data["statusText"] = "Success"
    data["name"] = "led OFF"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("Led OFF response Sent")
    return response

@app.route("/api/v1/ledon",methods=["OPTIONS", "GET"])
def ledon():
    print("led ON Called")
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18, GPIO.OUT)
    #GPIO.output(18, GPIO.HIGH)
    #pixels = neopixel.NeoPixel(board.D18, 150, brightness = 1.0)
    pixels.fill((0, 255, 0))

    data = {}
    data["Name"] = "skorboard"
    data["Response"] = "led response"
    data["status"] = "1"
    data["statusText"] = "Success"
    data["name"] = "led ON"
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("Led ON response Sent")
    return response

@app.route("/changeAllLeds", methods=["POST"])
def leds():
    content = request.get_json()
    for led in content:
        changeLed(led["num"], led["r"], led["g"], led["b"])
    return "ok"
    
def changeLed(num, r, g, b):
    print ("set color")
    print (r)
    print (g)
    print (b)
    pixels.fill((r, b, g))



@app.route("/api/v1/keys/<action>")
def btnVirtualKey(action):
    print("Nymeric Btn Called")
    if action == "fSlash":
        action = "/"
    if action == "dot":
        action = "."

    keyboard.write(action, exact=True)
    data = {}
    data["Name"] = "skorboard"
    data["Response"] = action
    response = jsonify(data)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print(action + " response Sent")
    return response

@app.route("/api",methods=["GET"])
def word_predictor():
    d = {}
    text = str(request.args["Query"])
    text = text[::-1]
    d["Query"] = text
    response = jsonify(d)
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    print("api Called")
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8050, debug=True)
