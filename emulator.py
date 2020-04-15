import os
import subprocess
import time

from adb_script import ADB


class Emulator:
    adb_shell = None

    @classmethod
    def start_emulator(cls):
        print("Start the emulator")
        # put your emulator bin to here.
        subprocess.Popen(['/Users/Nick/Library/Android/sdk/emulator/emulator', '-avd', 'Pixel_XL_API_23'])
        # wait for emulator
        time.sleep(20)
        print("Init ADB server")
        cls.adb_shell = ADB()
        cls.adb_shell.device.shell("wait-for-device")

        return cls.adb_shell

    @staticmethod
    def shutdown_emulator():
        print("Shutdown the emulator after 3 second...")
        time.sleep(3)
        os.system("adb emu kill")


if __name__ == '__main__':
    pass

# shell = Emulator.start_emulator()

# shell.list_all_package()