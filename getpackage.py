from androguard.misc import AnalyzeAPK
import sys
a,d,dx = AnalyzeAPK(sys.argv[1])

print(f"{a.get_package()}/{a.get_main_activity()}")
