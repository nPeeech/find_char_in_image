import numpy as np
from PIL import ImageFont, ImageDraw, Image
import cv2

fonts = ['msmincho.ttc','msgothic.ttc','HGRME.TTC','yumin.ttf']

def gen_char_imgs(character, fonts,font_size):
    # 表示する色
    b,g,r,a = 0,0,0,0 #B(青)・G(緑)・R(赤)・A(透明度)
    position = (0, 0) # テキスト表示位置
    imgs=[]
    
    for font_name in fonts:
        fontpath ='C:\Windows\Fonts\\'+font_name # Windows10 だと C:\Windows\Fonts\ 以下にフォントがあります。
        font = ImageFont.truetype(fontpath, font_size) # フォントサイズが32

        # img_pil = Image.fromarray(img) # 配列の各値を8bit(1byte)整数型(0～255)をPIL Imageに変換。
        img_pil = Image.new('RGB', (font_size, font_size),(230,230,230))

        draw = ImageDraw.Draw(img_pil) # drawインスタンスを生成

        draw.text(position, character, font = font , fill = (b, g, r, a) ) # drawにテキストを記載 fill:色 BGRA (RGB)
    
        img = np.array(img_pil) # PIL を配列に変換
        imgs.append(img)

    return imgs

def main():
    imgs = gen_char_imgs('ふ', fonts)

    for img in imgs:

        ## 表示
        cv2.imshow("res", img)
        # cv2.imwrite("img.jpg", img)

        cv2.waitKey(0)

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

