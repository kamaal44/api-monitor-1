import sys

import frida


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))


jscode = """

Java.perform(function() {
   var main = Java.use("com.example.testfrida.MainActivity");
  
  
   main.hello_a.implementation = function() {
     send("call hello_a");
     return this.getRunningAppProcesses.apply(this, arguments);
   };
  
   main.hello_b.implementation = function() {
     send("call hello_b");
     return this.getRunningAppProcesses.apply(this, arguments);
   };
  
   main.hello_c.implementation = function() {
     send("call hello_c");
     return this.getRunningAppProcesses.apply(this, arguments);
   };





});

"""

dev = frida.get_remote_device()

session = dev.attach("com.example.testfrida")

script = session.create_script(jscode)

script.on('message', on_message)

script.load()

sys.stdin.read()
