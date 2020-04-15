from androguard.misc import AnalyzeAPK


class Apkinfo:

    def __init__(self, apk_path):
        print(f"Init {apk_path}")
        apk, dalvikvmformat, analysis = AnalyzeAPK(apk_path)
        self._packageName = apk.get_package()
        self._mainActivity = apk.get_main_activity()
        print(f"packageName {self._packageName}")
        print(f"MainActivity {self._mainActivity}")

    @property
    def package_name(self):
        return self._packageName

    @property
    def main_activity(self):
        return self._mainActivity
