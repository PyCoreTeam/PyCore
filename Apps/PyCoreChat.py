import socket
def server(port : int, max: int) -> None:
    """PORT -> 本地端口，如果想让不在同一个局域网的人连接请使用FRP或者服务器。
    MAX -> 能连接的最大人数"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", port))
    s.listen(max)
    clients = []




