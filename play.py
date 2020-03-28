#!/usr/bin/env python3

import time

if __name__ == '__main__':
    f = open('./effect.txt', 'r')
    for line in f:
        print(line, end = '')
        if len(line) < 5:
            print('\033[0;0H')
            time.sleep(1/60)
    f.close()

