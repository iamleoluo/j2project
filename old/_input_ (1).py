import numpy as np
import cv2
pic = input("輸入的圖片檔名：")
#引進圖片檔
img = cv2.imread(pic)
imgGray = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
print(img.shape)
prec = int(input("精準度（1~4，建議2）："))
pers = int(input("取__％，建議10："))