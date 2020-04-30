import sys
import codecs

import frida


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))


dev = frida.get_remote_device()

session = dev.attach("com.example.myapplication")

with codecs.open('scripts/api_monitor.js', 'r', 'utf-8') as f:
    source = f.read()

script = session.create_script(source)

script.on('message', on_message)

script.load()

sys.stdin.read()
