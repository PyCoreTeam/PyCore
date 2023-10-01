# PyCore
A high freely toolbox
##  HTS命令使用
### ATK(攻击组合)
#### HttpAttack
##### 方法名:sendPacketAttack  
HTTP包  
用法: atk <主机(ip)> <端口> <线程> <失败*次后停止攻击>    
主机可选择是否携带超文本传输协议(http/https),自动添加。  
如果路径下有proxies.txt,则使用其中的代理  
#### TcpAttack
##### 方法名:tckAttack  
用法: tcpatk <主机(ip)> <端口> <线程> <包大小>  
包大小为 Count * 140个字节  
主机可选择是否携带超文本传输协议(http/https),自动添加。
TCP包  （不完整）  

##### 方法名:sockFullAttack  
完整的TCP包  
用法:fullatk <主机(ip)> <端口> <线程>  
主机自动转数字ip

#### 其他攻击  
##### 方法名:synAttackBetter  
SYN包(SCAPY加强)  
用法: bsynatk <主机(ip)> <目标iP> <线程>  
  
##### 方法名:synAttack    
SYN包    
用法: synatk <主机ip> <本机端口> <目标ip> <目标端口> <线程>  
