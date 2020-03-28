#!/usr/bin/env python3 

import cv2, os

def convert_frame(gray):
    """ arr(720, 960) -> (36, 48) """
    retmat = [['?' for i in range(0, 48)] for j in range(0, 36)]
    (blkh, blkw) = (720 // 36, 960 // 48)
    fillstr = '.^#*@'
    samples = [(5, 5), (5, 15), (10, 10), (15, 5), (15, 15)]
    coff = (len(fillstr) - 1) / (255 * len(samples))
    for r in range(0, 720, blkh):
        for c in range(0, 960, blkw):
            # for each block:
            gsum = 0
            for (rr, cc) in samples:
                gsum += gray[r+rr][c+cc]
            retmat[r // blkh][c // blkw] = fillstr[int(coff * gsum)]
    return retmat

def print_char_frame(cfrm):
    if os.name == 'posix':
        print('\033[0;0H') # reset cursor position at (0,0)
    else: # Windows
        print('')
    for r in range(0, len(cfrm)):
        for c in range(0, len(cfrm[r])):
            print(cfrm[r][c], end = ' ')
        print('')

if __name__ == '__main__':
    if not os.path.exists('./badapple.mp4'):
        print("""BadApple video file not found.
                Go download https://wshtan.net/ar/badapple.mp4 first""")
        exit()
    cap = cv2.VideoCapture('./badapple.mp4')
    # Or: cap = cv2.VideoCapture('https://wshtan.net/ar/badapple.mp4') # It's OK!
    while True:
        ret, frm = cap.read() # typeof ret, frm == 'bool, numpy.ndarray'
        if not ret:
            print('Video stream disconnected')
            break
        gray = cv2.cvtColor(frm, cv2.COLOR_BGR2GRAY) # gray.shape == (720, 960)
        print_char_frame(convert_frame(gray))
    cap.release()
