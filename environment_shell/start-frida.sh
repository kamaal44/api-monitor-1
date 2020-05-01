# start the frida

adb push environment_shell/frida-server /data/local/tmp/frida-server

adb shell chmod 755 /data/local/tmp/frida-server

adb shell /data/local/tmp/frida-server &
