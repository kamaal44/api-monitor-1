import sys
import time

from apkinfo.apkinfo import Apkinfo
from emulator.emulator import Emulator

if len(sys.argv) == 2:
    # Start the Emulator
    adb_shell = Emulator.start_emulator()

    apk_filepath = sys.argv[1]
    apkinfo = Apkinfo(apk_filepath)

    # install
    adb_shell.install_apk(apk_filepath)

    # start run apk
    adb_shell.start_apk(apkinfo.package_name, apkinfo.main_activity)

    time.sleep(10)

    adb_shell.clean()

    Emulator.shutdown_emulator()

else:
    print("Usage: python main.py test.apk")
