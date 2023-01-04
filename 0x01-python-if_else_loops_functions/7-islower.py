#!/usr/bin/python3
def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        check = ord(c)
        if check >= 97 and check <= 122:
            return True
        else:
            return False
