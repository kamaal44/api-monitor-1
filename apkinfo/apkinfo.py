from androguard.misc import AnalyzeAPK


class Apkinfo:

    def __init__(self, apk_path):
        print(f"Init {apk_path}")
        self.apk, self.dalvikvmformat, self.analysis = AnalyzeAPK(apk_path)
        # get package name and the main launch activity to start the app.
        self._packageName = self.apk.get_package()
        self._mainActivity = self.apk.get_main_activity()

    @property
    def package_name(self):
        return self._packageName

    @property
    def main_activity(self):
        return self._mainActivity

    def get_android_api(self):
        """
        Returns a list of Android APIs call.
        :return: (class_name, method_name)
        """
        method_analysis = self.analysis.get_android_api_usage()
        for meth in method_analysis:
            yield meth.class_name, meth.name

    def launch_activity(self):
        return f"{self._packageName}/{self._mainActivity}"


if __name__ == '__main__':
    pass

    # apk = Apkinfo("app-debug.apk")
    #
    # for i in apk.get_android_api():
    #     print(i)
