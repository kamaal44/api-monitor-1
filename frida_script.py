import codecs
import frida
import sys
import os
import time
import threading
from apkinfo.apkinfo import Apkinfo


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {}".format(message['payload']))


def stdinLoop():
    sys.stdin.read()


apk_filepath = sys.argv[1]
apkinfo = Apkinfo(apk_filepath)

# install app

os.system(f"adb install -r {apk_filepath}")

os.system(f"adb shell am start -n {apkinfo.launch_activity()}")

dev = frida.get_remote_device()

session = dev.attach(apkinfo.package_name)

with codecs.open('frida_scripts/api_monitor.js', 'r', 'utf-8') as f:
    source = f.read()

script = session.create_script(source)
script.on('message', on_message)
script.load()

stdinTh = threading.Thread(target=stdinLoop, name="stdinTh")
stdinTh.daemon = True
stdinTh.start()

time.sleep(5)

sys.exit()
