import _thread
import os
import sys
from PyCoreHackToolUtils import *

import logging


# 由StarryCamile(Yurnu)编写的代码由CodeGeeX编写注释

# 待办清单
# line 109 ： 告诉用户缺了什么 【4*】

def create_config():
    # 如果配置文件不存在，则创建一个
    f = open(SELF_CONF_PATH, "x")
    # 初始化配置文件
    initConfig(CONFIG)
    # 关闭文件
    f.close()


def main():
    try:
        # 尝试检查配置文件是否存在
        if not os.path.exists(SELF_CONF_PATH):
            create_config()
    except:
        # 如果检查到异常，则删除配置文件
        os.remove(SELF_CONF_PATH)
        create_config()
    else:
        # 启动新的线程，重置配置文件
        _thread.start_new_thread(resetToNewConfig, (CONFIG,))
    while True:
        # 获取用户输入
        cmd = str(input("PyCore@HackTool -> ")).split(" ")
        try:
            # 如果用户输入的命令是atk
            if cmd[0] == "atk":
                # 发送数据包攻击
                sendPacketAttack(
                    toRequestUrl([cmd[1]]), int(str(cmd[2])), failnum=int(cmd[3])
                )
            # 如果用户输入的命令是exit
            elif cmd[0] == "exit":
                # 退出程序
                sys.exit("Exited.")
            # 如果用户输入的命令是ps
            elif cmd[0] == "ps":
                # 如果用户输入的参数是clear#
                if cmd[1] == "clear":
                    try:
                        # 尝试删除文件
                        os.remove("./proxies.txt")
                    except:
                        # 如果删除失败，则跳过
                        pass
                # 如果用户输入的参数是get
                elif cmd[1] == "get":
                    # 获取代理
                    print(getProxies())
                # 如果用户输入的参数是to
                elif cmd[1] == "to":
                    # 转换代理
                    print(proxiesTo(cmd[2], cmd[3]))
            # 如果用户输入的命令是tcpatk
            elif cmd[0] == "tcpatk":
                # 发送TCP攻击
                tcpAttack((cmd[1], int(cmd[2])), int(cmd[3]))
            elif cmd[0] == "gui":
                colormsg("Gui",'red')
                app = QApplication(sys.argv)
                ex = HackToolMainUi.Example()
                app.exec_()
                ex.setVisible(True)


            # 如果用户输入的命令是fullatk
            elif cmd[0] == "fullatk":
                # 发送FULL攻击
                tcpAttack((cmd[1], int(cmd[2])), int(cmd[3]))
            # 如果用户输入的命令是synatk
            elif cmd[0] == "synatk":
                # 发送SYN攻击
                synAttack(cmd[1], int(cmd[2]), cmd[3], int(cmd[4]), int(cmd[5]))
            # 如果用户输入的命令是bsynatk
            elif cmd[0] == "bsynatk":
                # 发送BETTER SYN攻击
                synAttackBetter(cmd[1], cmd[2], int(cmd[3]))
            # 如果用户输入的命令是udpatk
            elif cmd[0] == "udpatk":
                # 发送UDP攻击
                udpAttack(
                    cmd[1].lower().replace("http://", "").replace("https://", ""),
                    int(cmd[2]),
                    int(cmd[3]),
                )
            # 如果用户输入的命令是sshatk
            elif cmd[0] == "sshatk":
                # 发送SSH攻击
                sshAttack(cmd[1], int(cmd[2]), int(cmd[3]))
            # 如果用户输入的命令是set
            elif cmd[0] == "set":
                # 如果用户输入的参数是reset
                if cmd[1] == "reset":
                    # 初始化配置文件
                    initConfig(CONFIG)
            # 如果用户输入的命令是其他
            else:
                # 如果用户输入的参数不为空
                if cmd != "\n":
                    # 打印错误信息
                    # 添加人性化设计
                    logger.warning(f"意外的命令错误{cmd},请检查您的输入", "yellow")
        # 如果用户输入的参数不完整
        # Q:TODO （困难）告诉用户缺了什么 in 109 A:你这种思想还是太城市化了

        except IndexError:
            logger.warning("参数不完整。请检查您的参数是否有缺漏")
        except (ValueError, TypeError):
            # 打印错误信息，另存为log文件
            logging.basicConfig(
                level=logging.DEBUG,
                filename="error.log",
                filemode="a",
            )
            logger.error("Error!", exc_info=True)
            logger.error("错误信息已保存至log文件。")


# 我也不知道干嘛的，那就凑个字数罢（
main()
