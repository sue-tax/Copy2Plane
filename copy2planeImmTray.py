'''
Created on 2025/11/24
version 0.04
@author: sue-t
'''
from pystray import Icon, MenuItem, Menu
from PIL import Image
import threading
import pyperclip
import sys
import time

class taskTray:
    def __init__(self, image):
        image = Image.open(image)
        menu = Menu(
                # MenuItem('加工', self.doProc),
                MenuItem('終了', self.doExit),
        )
        self.icon = Icon(name='copy2plane', title='copy2plane',
                icon=image, menu=menu)

    def doExit(self, _icon):
        pyperclip.copy("\n")
        self.icon.stop()

    def run(self):
        self.task_thread = threading.Thread(target=self.proc)
        self.task_thread.start()
        self.icon.run()

    def waitForNewPaste(self):
        old = pyperclip.paste()
        while True:
            time.sleep(0.1)
            new = pyperclip.paste()
            if new != old:
                return new

    def proc(self):
        while True:
            try:
                src = self.waitForNewPaste()
            except Exception as _:
                time.sleep(0.1)
                continue
            
            dst = src.replace(',','') \
                    .replace('\t','') \
                    .replace('\r\n','') \
                    .replace('\n','') \
                    .replace(' ','') \
                    .replace(chr(165), '') \
                    .replace('△', '-') \
                    .replace('▲', '-')
            if dst == '-':
                dst = '0'
    
            while True:
                try:
                    pyperclip.copy(dst)
                    self.icon.notify(f"{src}\n->\n{dst}",
                            "変換しました")
                    break
                except Exception as _:
                    time.sleep(0.1)
                    continue
    
            # 変換前が空でなく、変換後が空ならば終了
            # カンマ、タブ、改行だけをコピーした場合に、終了
            # Excelで２つの空のセルをコピーすることを想定
            if (src != '') and (dst == ''):
                self.icon.notify("終了します")
                self.doExit(self.icon)
                sys.exit()
            time.sleep(1)

if __name__ == '__main__':
    tray = taskTray(image="copy2plane.jpg")
    tray.run()

