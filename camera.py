# OpenCV のインポート
import cv2
import numpy as np
import time
import generate_char_img as gci

# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
cap = cv2.VideoCapture(0)
threshold = 0.52
# w, h = temp.shape[::-1]
WIDTH = 1280
HEIGHT = 720
FPS = 30
cap.set(cv2.CAP_PROP_FPS, FPS)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
fonts = ['msmincho.ttc','msgothic.ttc','HGRME.TTC','yumin.ttf']
print("search_char(len=1) >> ",end='')
search_char = input()
print("font_size >> ",end='')
font_size = int(input())
template_imgs = gci.gen_char_imgs(search_char,fonts,font_size) 
for template_img in template_imgs:
    cv2.imshow('template', template_img)
    cv2.waitKey(1000)
cv2.destroyAllWindows()
w, h = font_size, font_size

print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    for template_img in template_imgs:
        template_img = cv2.cvtColor(template_img, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(frame_gray, template_img, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    cv2.imshow('Frame', frame)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break
    
# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()