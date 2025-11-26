'''
Created on 2025/11/24
version 0.03
@author: sue-t
'''
import pyperclip
import sys
import time

if __name__ == '__main__':
    while True:
        try:
            src = pyperclip.waitForNewPaste()
        except Exception as e:
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
                break
            except Exception as e:
                time.sleep(0.1)
                continue

        # 変換前が空でなく、変換後が空ならば終了
        # カンマ、タブ、改行だけをコピーした場合に、終了
        # Excelで２つの空のセルをコピーすることを想定
        if (src != '') and (dst == ''):
            sys.exit()