import os
import subprocess
from shutil import copy

from PyCoreHackToolUtils import colormsg
colormsg("&&&--- PyCore.HackTool.Builder ---&&&",'red')
copy('PyCore.HackTool.py', './PyCore.AutoBuild/')
copy('PyCoreHackToolUtils.py', './PyCore.AutoBuild/')
Username = str(input("USERNAME: "))
pwd = str(input("PASSWORD: "))
with open("./PyCore.AutoBuild/PyCore.HackTool.py",'a+') as f:
    f.write(f"name1 = '{Username}'")
    f.write(f"\npwd1 = '{pwd}'")
    f.write(f"\nmain()")
    f.close()
os.system("nuitka PyCore.AutoBuild\PyCore.HackTool.py --mingw64 --onefile ")
