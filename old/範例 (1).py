import numpy as np
import cv2
#引進圖片檔
img = cv2.imread('dog.jpg')

#引進灰階圖片檔
imgGray = cv2.imread('dog.jpg', cv2.IMREAD_GRAYSCALE)
import img_gray

print(img_gray.gray)
print(imgGray)
print("i'm colorful")
print(img)
#顯示numpy的陣列大小
print(img.shape)

#顯示圖片(暫時不用在mac上會當機)
#cv2.imshow('m',img)

#輸出圖片cv2.imwrite(檔名,陣列,參數(品質0~100))
cv2.imwrite('output.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,100])

#輸出圖片cv2.imwrite(檔名,陣列,參數(png壓縮層級0~9))
cv2.imwrite('output.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])




