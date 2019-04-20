import numpy as np
import cv2
import _input_
import imgAnalysisGray
img = imgAnalysisGray.img
imgGray = imgAnalysisGray.imgGray
print("")
#引進下一個分析檔案
import imgAnalysisColors

#輸出圖片cv2.imwrite(檔名,陣列,參數(品質0~100))
cv2.imwrite('output.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,100])

#輸出圖片cv2.imwrite(檔名,陣列,參數(png壓縮層級0~9))
cv2.imwrite('output.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])

cv2.imwrite('outputGray.jpg',imgGray)
