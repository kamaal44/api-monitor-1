import codecs
import frida
import subprocess
import sys
import os




def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {}".format(message['payload']))

os.system("adb shell am start -n bmthx.god102409paperi/bmthx.god102409paperi.Begin")

dev = frida.get_remote_device()

session = dev.attach(sys.argv[1])

with codecs.open('frida_scripts/api_monitor.js', 'r', 'utf-8') as f:
    source = f.read()


script = session.create_script(source)

script.on('message', on_message)

script.load()

print("send back key")
os.system("adb shell input keyevent 04")

print("restart app")
os.system("adb shell am start -n bmthx.god102409paperi/bmthx.god102409paperi.Begin")

sys.stdin.read()
