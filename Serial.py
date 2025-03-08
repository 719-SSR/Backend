

import serial
from serial.tools import list_ports
"""
̛̛̾̒̊̈̈̇ͭ̾҉̱̹͙ ̪̖̠̱ͧͬͤͯ̄ͣͨ̚̚͘͠ ̵̸̶̶̸̨̼̜͕͍͈͔̪̘̣̮̖̥̗̪̬͓̠̲̟̻̞̤̳͔͖̥̻͉̮͓̬͓̤̩͉̻̩̘͕̠͍̳̳͔̣̬̰̤̺̹͉̞͚̖̲͈̻̪̜̹͇̭̥̼̹ͮͫ͐̄͐ͯ̑͊ͤͩͬ͛͛̆̐̐͗́̔̊͋̈̐ͥͪ̽ͣͪ̒́̀ͤͬ̃̄̆̈́ͭͣ̇̓̊ͦ̍ͭ͂̽͑ͫ́̽͒̇̾͊ͮͪ̑͑̄̕̕͘͜͢͟͞͝͝͡ͅͅ.̢̬̜͇̳̣̮̩̗͈̝̪̭̲̓̆̄̒̈̊ͧ̈́̋ͥͬ̏͑ͨ͗̿ͨ̃ͧ͒͑̈̚̚҉͖̭̦̲̣͎̗̳̾̓̉̂͑͛ͧ̾̕͞ ͆̆̏̋̄ͤ͏̧̨̧̡̛̳͙͙͚̮̥̙̖̞͈̜͖̱̻̪̗̱̠̼͈̠͔̯̺̳̥͔̱̟̱̥̣͎̫̰̣͕͆̀̈̓̃͋̐̓ͥ̀̐̐̽̑ͦ͑͗͑̄ͥ͒̀̚͟͜͜͡͞͞ͅͅ.̷͎̱̫̗̗̹̥̟̬̲̲͉͇͉̦̼̞͆̾͑̓͛̀̒͆͆͑ͯ͋ͭͬͤ̏ͬͮͤ͘͠͏̸͏̵̬̰̹̬̘͍͖̤̮̮̣͇̥͉̹̝̰͕̼̫̣͔͙̫̋ͬ̇̅ͤ̀̚ͅ҉̷̸̷̨͍̺̟̳͔̞̙̳̳͕͖̬̮̳̥͇͚̝̘̞̯̦͂̿͆ͯ̋̒̇ͨ́͋̄̃͌̉̈ͮ̿̾ͬ̋̌̂͑ͤ̓ͭ̀͒̌̑̒̎͊͆ͬͬ͟͠҉̶̴̩̥͎͖̻̜̰̪̙̝̺͕͓̹̱͚̪ͦͣ͐́͆̀̀ͪ̍ͫ͂̇ͬ̑̉̓̍̋ͦ͗̌̌̊͊̊́̚͞.̢͔̮̖̠͇̝̳̪̩̩̥͎͔̞̳̣̻͓̜͍͍̐̊̔́̀͛̎̑͌̓͑̿́̏ͭͫ̀͋͋̐̍ͦͦ̀̄̕̚ͅͅ ̷̷̨̦̖̘̤̱̮̘̪̘̘̦͖̪̟̱̥̟͓̇ͣ̿͗͆̓͆̈́ͨ̓ͫ̆̓ͯ̿̔̑ͧ͛̽ͅ͏̡͇͎̳̣̹̀ͭ̿̂ͩ͑̇̕͟҉̨̠͈̼̲̣̣͖̠͓̞̞̄̾.̵̥͈̝͚̘̣̘͍̘͎̟̳̺̗̬̰̤̪̮̞̝̯̣̖̂̿ͫͣ̊̔ͯ́̋̍͞͠҉̴̧̡̛̲̗̭̫͈̺̗̗̭̮͎̗̫̫͉͉͇͚͎͓̦͊ͤ͋͐́̋̃͛̔͒̒ͥ̇͂̽̌̈̎̀͆͑͆ͨͬ̽͌̍̀̚͘͘͡͡ͅ͏̶̢̘͈̪̗̙̩͚̜̳̘̖͇̲̓̐͂͆ͬͧ́̅͋̍́́́͡ͅ.̡̲̤̯͇̟ͯͪ̽̿ͯ̍ͤ̀҉̷̸̨͍̺̟̳͔̞̙̳̳͕͖̬̮̳̥͖͕͂̿͆ͯ̋̒̇ͨ́͋̄̃͌̉̈ͮ̿͟͠ ̷͇͚̝̘̞̯̦̾ͬ̋̌̂͑ͤ̓ͭ̀͒̌̑̒̎͊͆ͬͬ҉̶̴̩̥͎͖̻̜̰̪̙̝̺͕͓̹̱͚̪̱ͦͣ͐́͆̀̀ͪ̍ͫ͂̇ͬ̑̉̓̍̋ͦ͗̌̌̊͊̊́̚͞.̢͔̮̖̠͇̝̳̪̩̩̥͎͔̞̳̣̻͓̜͍͍̐̊̔́̀͛̎̑͌̓͑̿́̏ͭͫ̀͋͋̐̍ͦͦ̀̄̕̚ͅͅ ̷̷̨̦̖̘̤̱̮̘̪̘̘̦͖̪̟̱̇ͣ̿͗͆̓͆̈́ͨ̓ͫ̆̓ͅ[ ̝̦̬̤͖̗͕͎͊̐̊͊̏ͦ̈́̒͆́ͬ̂̕͠ ̛̛̾̒̊̈̈̇ͭ̾҉̱̹͙ ̪̖̠̱ͧͬͤͯ̄ͣͨ̚̚͘͠ ̵̸̶̶̸̨̼̜͕͍͈͔̪̘̣̮̖̥̗̪̬͓̠̲̟̻̞̤̳͔͖̥̻͉̮͓̬͓̤̩͉̻̩̘͕̠͍̳̳͔̣̬̰̤̺̹͉̞͚̖̲͈̻̪̜̹͇̭̥̼̹ͮͫ͐̄͐ͯ̑͊ͤͩͬ͛͛̆̐̐͗́̔̊͋̈̐ͥͪ̽ͣͪ̒́̀ͤͬ̃̄̆̈́ͭͣ̇̓̊ͦ̍ͭ͂̽͑ͫ́̽͒̇̾͊ͮͪ̑͑̄̕̕͘͜͢͟͞͝͝͡ͅͅ.̢̬̜͇̳̣̮̩̗͈̝̪̭̲̓̆̄̒̈̊ͧ̈́̋ͥͬ̏͑ͨ͗̿ͨ̃ͧ͒͑̈̚̚҉͖̭̦̲̣͎̗̳̾̓̉̂͑͛ͧ̾̕͞ ͆̆̏̋̄ͤ͏̧̨̧̡̛̳͙͙͚̮̥̙̖̞͈̜͖̱̻̪̗̱̠̼͈̠͔̯̺̳̥͔̱̟̱̥̣͎̫̰̣͕͆̀̈̓̃͋̐̓ͥ̀̐̐̽̑ͦ͑͗͑̄ͥ͒̀̚͟͜͜͡͞͞ͅͅ.̷͎̱̫̗̗̹̥̟̬̲̲͉͇͉̦̼̞͆̾͑̓͛̀̒͆͆͑ͯ͋ͭͬͤ̏ͬͮͤ͘͠͏̸͏̵̬̰̹̬̘͍͖̤̮̮̣͇̥͉̹̝̰͕̼̫̣͔͙̫̋ͬ̇̅ͤ̀̚ͅ҉̷̸̷̨͍̺̟̳͔̞̙̳̳͕͖̬̮̳̥͇͚̝̘̞̯̦͂̿͆ͯ̋̒̇ͨ́͋̄̃͌̉̈ͮ̿̾ͬ̋̌̂͑ͤ̓ͭ̀͒̌̑̒̎͊͆ͬͬ͟͠҉̶̴̩̥͎͖̻̜̰̪̙̝̺͕͓̹̱͚̪ͦͣ͐́͆̀̀ͪ̍ͫ͂̇ͬ̑̉̓̍̋ͦ͗̌̌̊͊̊́̚͞.̢͔̮̖̠͇̝̳̪̩̩̥͎͔̞̳̣̻͓̜͍͍̐̊̔́̀͛̎̑͌̓͑̿́̏ͭͫ̀͋͋̐̍ͦͦ̀̄̕̚ͅͅ ̷̷̨̦̖̘̤̱̮̘̪̘̘̦͖̪̟̱̥̟͓̇ͣ̿͗͆̓͆̈́ͨ̓ͫ̆̓ͯ̿̔̑ͧ͛̽ͅ͏̡͇͎̳̣̹̀ͭ̿̂ͩ͑̇̕͟҉̨̠͈̼̲̣̣͖̠͓̞̞̄̾.̵̥͈̝͚̘̣̘͍̘͎̟̳̺̗̬̰̤̪̮̞̝̯̣̖̂̿ͫͣ̊̔ͯ́̋̍͞͠҉̴̧̡̛̲̗̭̫͈̺̗̗̭̮͎̗̫̫͉͉͇͚͎͓̦͊ͤ͋͐́̋̃͛̔͒̒ͥ̇͂̽̌̈̎̀͆͑͆ͨͬ̽͌̍̀̚͘͘͡͡ͅ͏̶̢̘͈̪̗̙̩͚̜̳̘̖͇̲̓̐͂͆ͬͧ́̅͋̍́́́͡ͅ.̡̲̤̯͇̟ͯͪ̽̿ͯ̍ͤ̀҉̷̸̨͍̺̟̳͔̞̙̳̳͕͖̬̮̳̥͖͕͂̿͆ͯ̋̒̇ͨ́͋̄̃͌̉̈ͮ̿͟͠ ̷͇͚̝̘̞̯̦̾ͬ̋̌̂͑ͤ̓ͭ̀͒̌̑̒̎͊͆ͬͬ҉̶̴̩̥͎͖̻̜̰̪̙̝̺͕͓̹̱͚̪̱ͦͣ͐́͆̀̀ͪ̍ͫ͂̇ͬ̑̉̓̍̋ͦ͗̌̌̊͊̊́̚͞.̢͔̮̖̠͇̝̳̪̩̩̥͎͔̞̳̣̻͓̜͍͍̐̊̔́̀͛̎̑͌̓͑̿́̏ͭͫ̀͋͋̐̍ͦͦ̀̄̕̚ͅͅ ̷̷̨̦̖̘̤̱̮̘̪̘̘̦͖̪̟̱̇ͣ̿͗͆̓͆̈́ͨ̓ ̝̦̬̤͖̗͕͎͊̐̊͊̏ͦ̈́̒͆́ͬ̂̕͠ ̛̛̾̒̊̈̈̇ͭ̾҉̱̹͙ ̪̖̠̱ͧͬͤͯ̄ͣͨ̚̚͘͠ ̵̸̶̶̸̨̼̜͕͍͈͔̪̘̣̮̖̥̗̪̬͓̠̲̟̻̞̤̳͔͖̥̻͉̮͓̬͓̤̩͉̻̩̘͕̠͍̳̳͔̣̬̰̤̺̹͉̞͚̖̲͈̻̪̜̹͇̭̥̼̹ͮͫ͐̄͐ͯ̑͊ͤͩͬ͛͛̆̐̐͗́̔̊͋̈̐ͥͪ̽ͣͪ̒́̀ͤͬ̃̄̆̈́ͭͣ̇̓̊ͦ̍ͭ͂̽͑ͫ́̽͒̇̾͊ͮͪ̑͑̄̕̕͘͜͢͟͞͝͝͡ͅͅ.̢̬̜͇̳̣̮̩̗͈̝̪̭̲̓̆̄̒̈̊ͧ̈́̋ͥͬ̏͑ͨ͗̿ͨ̃ͧ͒͑̈̚̚҉͖̭̦̲̣͎̗̳̾̓̉̂͑͛ͧ̾̕͞ ͆̆̏̋̄ͤ͏̧̨̧̡̛̳͙͙͚̮̥̙̖̞͈̜͖̱̻̪̗̱̠̼͈̠͔̯̺̳̥͔̱̟̱̥̣͎̫̰̣͕͆̀̈̓̃͋̐̓ͥ̀̐̐̽̑ͦ͑͗͑̄ͥ͒̀̚͟͜͜͡͞͞ͅͅ.̷͎̱̫̗̗̹̥̟̬̲̲͉͇͉̦̼̞͆̾͑̓͛̀̒͆͆͑ͯ͋ͭͬͤ̏ͬͮͤ͘͠͏̸͏̵̬̰̹̬̘͍͖̤̮̮̣͇̥͉̹̝̰͕̼̫̣͔͙̫̋ͬ̇̅ͤ̀̚ͅ҉̷̸̷̨͍̺̟̳͔̞̙̳̳͕͖̬̮̳̥͇͚̝̘̞̯̦͂̿͆ͯ̋̒̇ͨ́͋̄̃͌̉̈ͮ̿̾ͬ̋̌̂͑ͤ̓ͭ̀͒̌̑̒̎͊͆ͬͬ͟͠҉̶̴̩̥͎͖̻̜̰̪̙̝̺͕͓̹̱͚̪ͦͣ͐́͆̀̀ͪ̍ͫ͂̇ͬ̑̉̓̍̋ͦ͗̌̌̊͊̊́̚͞.̢͔̮̖̠͇̝̳̪̩̩̥͎͔̞̳̣̻͓̜͍͍̐̊̔́̀͛̎̑͌̓͑̿́̏ͭͫ̀͋͋̐̍ͦͦ̀̄̕̚ͅͅ ̷̷̨̦̖̘̤̱̮̘̪̘̘̦͖̪̟̱̥̟͓̇ͣ̿͗͆̓͆̈́ͨ̓ͫ̆̓ͯ̿̔̑ͧ͛̽ͅ͏̡͇͎̳̣̹̀ͭ̿̂ͩ͑̇̕͟҉̨̠͈̼̲̣̣͖̠͓̞̞̄̾.̵̥͈̝͚̘̣̘͍̘͎̟̳̺̗̬̰̤̪̮̞̝̯̣̖̂̿ͫͣ̊̔ͯ́̋̍͞͠҉̴̧̡̛̲̗̭̫͈̺̗̗̭̮͎̗̫̫͉͉͇͚͎͓̦͊ͤ͋͐́̋̃͛̔͒̒ͥ̇͂̽̌̈̎̀͆͑͆ͨͬ̽͌̍̀̚͘͘͡͡ͅ͏̶̢̘͈̪̗̙̩͚̜̳̘̖͇̲̓̐͂͆ͬͧ́̅͋̍́́́͡ͅ.̡̲̤̯͇̟ͯͪ̽̿ͯ̍ͤ̀҉̷̸̨͍̺̟̳͔̞̙̳̳͕͖̬̮̳̥͖͕͂̿͆ͯ̋̒̇ͨ́͋̄̃͌̉̈ͮ̿͟͠ ̷͇͚̝̘̞̯̦̾ͬ̋̌̂͑ͤ̓ͭ̀͒̌̑̒̎͊͆ͬͬ҉̶̴
"""
import struct
import time
import enum






class Data(enum.Enum):
    DEPTH = 7
    ATTITUDE = 5
    JOYSTICK = 6
    TEMPERATURE = 8
    SERVO = 9


class short :
    pass
class double :
    pass


class SerialProtocolHandler:
    def __init__(self, port, baudrate=115200):
        # 初始化串口
        self.ser = serial.Serial(port, baudrate)
        self.ser.flush()
        self.rxstate = 0  # 接收状态机的初始状态
        self.rx_id = 0     # 接收到的 ID
        self.rx_map = {  # 由类型组成的字典
            Data.DEPTH: [float],  # 深度
            Data.ATTITUDE: [float, float, float],  # Roll, Pitch, Yaw
            Data.JOYSTICK: [float, float, float, float, float, float, float, float, bool, bool, bool, bool, bool, bool, bool, bool],  # 手柄数据（用于调试）
            Data.TEMPERATURE: [short],  # 温度
            Data.SERVO: [double, double, double, double]  # 四个舵机的转动角度 分别是 左 右 后面的左右 后面的上下
        }

        self.sum1 = 0     # 校验和初始值
        self.check_low = 0
        self.check_high = 0
        self.rx_buffer = bytearray(256)  # 数据接收缓冲区
        self.data_len = 0
        self.data_cnt = 0

        self.data = {key: [] for key in self.rx_map.keys()}  # 用于存储接收到的数据

    def send_data(self, ID, float_data_list, bool_data_list):
        """
        发送符合协议的数据，包含帧头、数据区和校验和
        """
        if len(float_data_list) != 8 or len(bool_data_list) != 8:
            raise ValueError("必须提供 8 个 float 数据和 8 个 bool 数据")
        
        # 1. 帧头 0xAA, 0xBB
        Tx_buffer = bytearray(50)  # 假设最大数据包为 50 字节
        num = 0
        sum1 = 0

        Tx_buffer[num] = 0xAA
        sum1 += Tx_buffer[num]
        num += 1

        if ID == 0x06:
            Tx_buffer[num] = 0xBB
        else:
            Tx_buffer[num] = ID
        sum1 += Tx_buffer[num]
        num += 1

        # 2. 后面四十个字节：8 个 float（每个 4 字节）和 8 个 bool（每个 1 字节）
        data_bytes = []

        # 将每个 float 转换为字节流
        for float_value in float_data_list:
            data_bytes.extend(struct.pack('!f', float_value))  # 将浮动数转为 4 字节字节流

        # 将每个 bool 转换为字节流（1 字节）
        for bool_value in bool_data_list:
            data_bytes.append(struct.pack('B', bool_value)[0])  # 将布尔值转为 1 字节

        # 将数据添加到缓冲区
        for byte in data_bytes:
            Tx_buffer[num] = byte
            sum1 += byte
            num += 1

        # 3. 校验和：所有字节的和的最后 16 位
        checksum = sum1 & 0xFFFF
        checksum_low = checksum & 0xFF
        checksum_high = (checksum >> 8) & 0xFF

        # 4. 校验低字节和高字节
        Tx_buffer[num] = checksum_low
        Tx_buffer[num + 1] = checksum_high

        # 发送数据
        self.ser.write(Tx_buffer)
        print(f"Sent data: {Tx_buffer}")

    def receive_data(self):
        """
        接收数据并进行协议解析和校验
        """
        while True:
            # 从串口读取一个字节
            data = self.ser.read(1)
            if not data:
                continue  # 如果没有数据，跳过

            data = data[0]  # 将接收到的字节取出来

            if self.rxstate == 0 and data == 0xAA:
                # 帧头 0xAA
                self.rxstate = 1
                self.sum1 += data

            elif self.rxstate == 1 and data == 0xBB:
                # 帧头 0xBB
                self.rxstate = 2
                self.sum1 += data

            elif self.rxstate == 2:
                # 接收 ID
                self.rx_id = data
                self.rxstate = 3
                self.sum1 += data

            elif self.rxstate == 3:
                self.rx_data= []
                for values in self.rx_map[self.rx_id]:
                    if values == float:
                        data = self.ser.read(4)
                        self.rx_data.append(struct.unpack('!f', data)[0])
                        self.sum1 += sum(data)
                    elif values == bool:
                        data = self.ser.read(1)
                        self.rx_data.append(struct.unpack('B', data)[0])
                        self.sum1 += data[0]
                    elif values == short:
                        data = self.ser.read(2)
                        self.rx_data.append(struct.unpack('!h', data)[0])
                        self.sum1 += sum(data)
                    elif values == double:
                        data = self.ser.read(8)
                        self.rx_data.append(struct.unpack('!d', data)[0])
                        self.sum1 += sum(data)

                self.rxstate = 4

            elif self.rxstate == 4:
                # 接收校验低字节
                self.check_low = data
                self.rxstate = 5

            elif self.rxstate == 5:
                # 接收校验高字节
                self.check_high = data
                self.rxstate = 6

            elif self.rxstate == 6:
                # 校验和检查
                total_sum = sum(self.rx_buffer[:self.data_cnt])
                if total_sum == ((self.check_high << 8) | self.check_low):
                    # print(f"Valid data received: { self.rx_data }")

                    self.rxstate = 0
                    self.sum1 = 0
                    self.data_len = 0
                    self.data_cnt = 0
                    self.check_low = 0
                    self.check_high = 0
                    self.data[self.rx_id] = self.rx_data
                else:
                    self.rxstate = 0
                    self.sum1 = 0
                    self.data_len = 0
                    self.data_cnt = 0
                    self.check_low = 0
                    self.check_high = 0
                    print("Checksum error")
            else:
                # 其他状态，重置
                self.rxstate = 0

    def get_data(self, ID):
        return self.data[ID]

    def close(self):
        # 关闭串口
        self.ser.close()



def choose_serial_port():
    # 获取所有可用的串口
    ports = list(list_ports.comports())
    
    if len(ports) == 0:
        print("没有找到可用的串口设备。")
        return None
    
    # 显示所有可用串口及其信息
    print("可用的串口设备:")
    for i, port in enumerate(ports):
        print(f"{i + 1}: {port.device} - {port.description}")
    
    # 提示用户选择一个端口
    while True:
        try:
            choice = int(input("请输入要选择的串口编号: ")) - 1
            if 0 <= choice < len(ports):
                selected_port = ports[choice].device
                print(f"您选择了串口: {selected_port}")
                return selected_port
            else:
                print("无效的选择，请输入有效的编号。")
        except ValueError:
            print("无效输入，请输入数字。")


if __name__ == "__main__":
    port =  choose_serial_port()
    handler = SerialProtocolHandler(port, 115200)
    try:
        # 主线程可以做一些其他任务，或者等待两个线程完成
        while True:
            # 发送数据
            handler.send_data([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], [True, False, True, False, True, False, True, False])
            # 接收数据
            handler.receive_data()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Terminating program.")
    finally:
        handler.close()
        # send_thread.join()  # 等待发送线程结束
        # receive_thread.join()  # 等待接收线程结束
        
