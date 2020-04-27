# put is to your ~/.bash_profile
# source .bash_profile

export ANDROID_HOME=/Users/nick/Library/Android/sdk
export PATH=${PATH}:${ANDROID_HOME}/tools
export PATH=${PATH}:${ANDROID_HOME}/platform-tools

# start your adb server
adb start-server

# init frida for python

adb forward tcp:27042 tcp:27042
adb forward tcp:27043 tcp:27043

