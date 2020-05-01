from ppadb.client import Client as AdbClient


class ADB:

    def __init__(self):
        # Default is "127.0.0.1" and 5037
        self.client = AdbClient(host="127.0.0.1", port=5037)
        self.device = self.client.device("emulator-5554")
        # if not connect to adb server
        # type `./adb start-server` after `./emulator -avd Pixel_XL_API_23`
        self.package_name = None

    def install_apk(self, apk_filepath):
        print(f"Install {apk_filepath}")
        self.device.install(apk_filepath, reinstall=True)

    def list_all_package(self):
        print(self.device.shell("pm list packages -f"))

    def start_apk(self, package_name, main_activity):
        self.package_name = package_name
        print("Start running APK")
        command = f"am start -n {package_name}/{main_activity}"

        self.device.shell(command)

    def clean(self):
        # close the app
        print("Clean the apk")
        command = f"am force-stop {self.package_name}"
        self.device.shell(command)
        # delete the app
        self.device.uninstall(self.package_name)

    def init_frida(self):
        # push frida server
        self.device.push("frida-server", "/data/local/tmp/frida-server")
        # change the mod of frida-server
        self.device.shell("chmod 755 /data/local/tmp/frida-server")
        # exec frida server background
        # It might not work, manually needed.
        self.device.shell("/data/local/tmp/frida-server &")
