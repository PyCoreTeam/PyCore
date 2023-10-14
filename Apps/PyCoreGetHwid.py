

import psutil
import platform
import string
import hashlib
import wmi


def getMac():
    # mac地址
    w = wmi.WMI()
    cc = ""
    for mac in w.Win32_NetworkAdapter():
        cc += str(mac.MACAddress)
    return cc
def getBiosID():
    w = wmi.WMI()
    cc = ""
    for bios_id in w.Win32_BIOS():
        cc += bios_id.SerialNumber.strip()
    return cc
def genRandomLetters(len : int):
    from random import choice
    a = ''
    for i in range(1, len +1):
        a += choice(list(string.ascii_letters))
    return a
def genHwid():
    disk_info = psutil.disk_partitions()
    _info = ''

    for disk in disk_info:
        _info = _info + disk.device + disk.fstype + disk.mountpoint
    _info = (_info + getBiosID()+ platform.node() + platform.processor() + getMac())
    md5 = hashlib.md5()
    md5.update(_info.encode("utf-8"))
    hwid = md5.hexdigest()
    return hwid.upper()
print("注意，更换电脑或者更改Mac会导致HWID变化！")
print(f"你的HWID是 {genHwid()} 请保存好该HWID！")

