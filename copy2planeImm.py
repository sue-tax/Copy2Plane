'''
Created on 2025/11/24

@author: sue-t
'''
import pyperclip
import sys

if __name__ == '__main__':
    while True:
        src = pyperclip.waitForNewPaste()
        dst = src.replace(',','') \
                .replace('\t','') \
                .replace('\r\n','') \
                .replace('\n','')
        pyperclip.copy(dst)
        if dst == '':
            sys.exit()
