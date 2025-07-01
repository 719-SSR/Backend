import socket
from threading import Thread, Event
import json
import enum
from functools import partial


class Data(enum.Enum):
    DEPTH = 7
    ATTITUDE = 5
    JOYSTICK = 6
    TEMPERATURE = 8
    SERVO = 9


class UDPClient:
    def __init__(self, server_ip: str, server_port: int, local_port: int = 0):
        """
        初始化UDP客户端

        :param server_ip: 服务器IP地址
        :param server_port: 服务器端口
        :param local_port: 本地端口（可选，默认随机分配）
        """
        self.server_addr = (server_ip, server_port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(("", local_port))
        self.running = Event()
        self.running.set()
        self.recv_thread = Thread(target=self._recv_loop, daemon=True)
        self.recv_callback = None

        self.data = {
            Data.DEPTH: None,
            Data.ATTITUDE: None,
            Data.JOYSTICK: None,
            Data.TEMPERATURE: None,
        }

    def start(self, recv_callback):
        """
        启动接收线程，可传入回调函数处理收到的数据

        :param recv_callback: 回调函数，形如callback(data: bytes, addr: tuple)
        """
        self.recv_callback = partial(recv_callback, self)
        self.recv_thread.start()

    def _recv_loop(self):
        while self.running.is_set():
            try:
                data, addr = self.sock.recvfrom(4096)
                if self.recv_callback:
                    self.recv_callback(data, addr)
            except Exception:
                continue

    def send(self, data: bytes):
        """
        发送数据到服务器

        :param data: 要发送的数据，类型为bytes
        """
        self.sock.sendto(data, self.server_addr)

    def close(self):
        """
        关闭客户端
        """
        self.running.clear()
        self.sock.close()

    def get_socket(self):
        """
        获取底层socket对象句柄
        """
        return self.sock
    
    def get_data(self, data_type: Data):
        """
        获取指定类型的数据

        :param data_type: 数据类型，Data枚举值
        :return: 对应类型的数据，如果没有数据则返回None
        """
        data = self.data.get(data_type)
        if data:
            return [True] + data
        else:
            # 这里返回什么，取决于你的需求
            return [False, None]


# 示例用法
if __name__ == "__main__":

    def on_recv(self, data, addr):
        print(f"Received from {addr}: {data}")
        type = json.loads(data.decode("utf-8")).get("type", "str")
        self.data[type] = data

    client = UDPClient("192.168.1.101", 4567)
    client.start(on_recv)
    client.send(b"Hello, UDP Server!")
    import time

    time.sleep(2)
    client.close()
