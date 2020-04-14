from apkinfo import Apkinfo
from adb_script import ADB
import time
import sys

apk_filepath = sys.argv[1]

apkinfo = Apkinfo(apk_filepath)
adb_shell = ADB()

# install
adb_shell.install_apk(apk_filepath)

# start run apk
adb_shell.start_apk(apkinfo.package_name, apkinfo.main_activity)

#time.sleep(2)

#adb_shell.clean()

# adb_shell.init_frida()
