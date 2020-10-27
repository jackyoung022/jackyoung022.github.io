import cv2
import os
path = 'images/gallery/fulls/'
out_path = 'images/gallery/thumbs/'
size = (128,128)
files = os.listdir(path)
for f in files:
    pic = cv2.imread(path + f)
    pic = cv2.resize(pic, size, cv2.INTER_CUBIC)
    cv2.imwrite(out_path + f, pic)