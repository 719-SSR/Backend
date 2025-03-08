import pygame.joystick
import time
import threading

class JoyStick:
    def __init__(self):
        self.available = self.init()
        self.lock = threading.Lock()  # 用于线程同步
        self.axes = []
        self.buttons = []
        self.hats = []

    def init(self) -> bool:
        # pygame.init()
        pygame.joystick.init()
        pygame.display.init()
        pygame.event.pump()
        joystick_count = pygame.joystick.get_count()
        if joystick_count == 0:
            print("未检测到任何手柄。")
            return False
        # 假设使用第一个连接的手柄
        self.joystick = pygame.joystick.Joystick(0)
        self.joystick.init()
        print(f"已初始化手柄：{self.joystick.get_name()}")
        return True

    def update(self):
        # 处理事件队列，必要时更新状态
        pygame.event.pump()
        with self.lock:
            self.axes = [self.joystick.get_axis(i) for i in range(self.joystick.get_numaxes())]
            self.buttons = [self.joystick.get_button(i) for i in range(self.joystick.get_numbuttons())]
            self.hats = list(self.joystick.get_hat(0))

    def get(self):
        with self.lock:
            return {
                "available": True,
                "axes": self.axes,
                "buttons": self.buttons,
                "hats": self.hats
            }
    
    def get_used(self):
        with self.lock:
            return {
                "available": True,
                "axes": self.axes[:6],
                "buttons": self.buttons[:8],
                "hats": self.hats
            }

def get_joystick():
    joystick_instance = JoyStick()
    joystick_instance.update()
    return joystick_instance.get()

if __name__ == "__main__":
    joystick_instance = JoyStick()
    while True:
        time.sleep(0.01)
        joystick_instance.update()
        print(type(joystick_instance.get()))