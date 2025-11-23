'''
Created on 2025/11/23

@author: sue-t
'''

from pyhooked import Hook, KeyboardEvent
import pyperclip
import sys

def handle_events(args):
    if isinstance(args, KeyboardEvent):
        if args.current_key == 'V' \
                 and args.event_type == 'key down' \
                 and ('Lshift' in args.pressed_key \
                      or 'Rshift' in args.pressed_key) \
                 and ('Lcontrol' in args.pressed_key \
                      or 'Rcontrol' in args.pressed_key):
            # print("shift+ctrl+V")
            src = pyperclip.paste()
            # print(src)
            dst = src.replace(',','') \
                    .replace('\r\n','') \
                    .replace('\n','')
            pyperclip.copy(dst)
        if args.current_key == 'Q' \
                 and args.event_type == 'key down' \
                 and ('Lshift' in args.pressed_key \
                      or 'Rshift' in args.pressed_key) \
                 and ('Lcontrol' in args.pressed_key \
                      or 'Rcontrol' in args.pressed_key):
            sys.exit()

if __name__ == '__main__':
    hk = Hook()
    hk.handler = handle_events
    hk.hook()
