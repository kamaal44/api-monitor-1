from androguard.misc import AnalyzeAPK
def launch_activity(apk_filepath):

    a,d,dx = AnalyzeAPK(apk_filepath)

    return f"{a.get_package()}/{a.get_main_activity()}"
