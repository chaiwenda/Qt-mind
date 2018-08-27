# -*- coding: UTF-8 -*-

from PIL import Image
from PIL import ImageEnhance
import os

path = './image'
pathed = './imaged'
files = os.listdir(path)
for item in files:
    filename = os.path.join(path, item)
    savefile = os.path.join(pathed, item)
    # 原始图像
    image = Image.open(filename)
    # image.show()
    # 对比度增强  -->可用于PDF增强
    enh_con = ImageEnhance.Contrast(image)
    contrast = 2
    image_contrasted = enh_con.enhance(contrast)
    print(contrast)
    # image_contrasted.show()
    image_contrasted.save(savefile)
# 亮度增强
enh_bri = ImageEnhance.Brightness(image)
brightness = 1.5
image_brightened = enh_bri.enhance(brightness)
# image_brightened.show()

# 色度增强
enh_col = ImageEnhance.Color(image)
color = 1.5
image_colored = enh_col.enhance(color)
# image_colored.show()




# 锐度增强
enh_sha = ImageEnhance.Sharpness(image)
sharpness = 3.0
image_sharped = enh_sha.enhance(sharpness)
# image_sharped.show()
