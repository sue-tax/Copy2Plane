'''
Created on 2025/11/24
version 0.06
@author: sue-t
'''
from pystray import Icon, MenuItem, Menu
from PIL import Image
import pyperclip
import jaconv
import time

# 123abcXYZ１２３ｄｅｆＳＴＵあいうカキクｻｼｽ

class taskTray:
    def __init__(self, image):
        image = Image.open(image)
        menu = Menu(
                MenuItem('大文字→小文字', self.doLower),
                MenuItem('小文字→大文字', self.doUpper),
                MenuItem('英数字全角→半角', self.doJz2h),
                MenuItem('英数字半角→全角', self.doJh2z),
                MenuItem('ひらがな→カタカナ', self.doJhira2kata),
                MenuItem('カタカナ→ひらがな', self.doJkata2hira),
                MenuItem('カタカナひらがな→半角', self.doJkana2h),
                MenuItem('カタカナ→全角', self.doJkana2z),
                MenuItem('加工', self.doProc),
                MenuItem('終了', self.doExit),
        )
        self.icon = Icon(name='copy2planeET',
                title='copy2planeET',
                icon=image, menu=menu)

    def paste(self, src, dst):
        while True:
            try:
                pyperclip.copy(dst)
                # self.icon.notify(f"{src}\n->\n{dst}",
                #         "変換しました")
                break
            except Exception as _:
                time.sleep(0.1)
                continue
        self.icon.notify(f"{src}\n->\n{dst}",
                "変換しました")
        

    def doLower(self, _icon):
        src = pyperclip.paste()
        dst = src.lower()
        self.paste(src, dst)

    def doUpper(self, _icon):
        src = pyperclip.paste()
        dst = src.upper()
        self.paste(src, dst)

    # 英数字を全角から半角に
    def doJz2h(self, _icon):
        src = pyperclip.paste()
        dst = jaconv.z2h(src, kana=False, ascii=True, digit=True)
        self.paste(src, dst)

    # 英数字を半角から全角に
    def doJh2z(self, _icon):
        src = pyperclip.paste()
        dst = jaconv.h2z(src, kana=False, ascii=True, digit=True)
        self.paste(src, dst)

    def doJhira2kata(self, _icon):
        src = pyperclip.paste()
        dst = jaconv.hira2kata(src)
        self.paste(src, dst)

    def doJkata2hira(self, _icon):
        src = pyperclip.paste()
        dst = jaconv.kata2hira(src)
        self.paste(src, dst)

    # ひらがな・カタカナを全角から半角に
    def doJkana2h(self, _icon):
        src = pyperclip.paste()
        src2 = jaconv.hira2kata(src)
        dst = jaconv.z2h(src2, kana=True, ascii=False, digit=False)
        self.paste(src, dst)

    # カタカナを半角から全角に
    def doJkana2z(self, _icon):
        src = pyperclip.paste()
        dst = jaconv.h2z(src, kana=True, ascii=False, digit=False)
        self.paste(src, dst)

    def doProc(self):
        src = pyperclip.paste()
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
        self.paste(src, dst)

    def doExit(self, _icon):
        self.icon.stop()

    def run(self):
        self.icon.run()

if __name__ == '__main__':
    tray = taskTray(image="copy2plane.jpg")
    tray.run()

