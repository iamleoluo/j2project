import inputDemo
import cv2
import numpy as np
import math
#--------讀取數據---------------
f = open("imgAnalysis1.txt","r")
imgAnalysis1 = f.readlines()
colors = imgAnalysis1[0].split("\t")
colors.pop(10)
print(colors)
good = imgAnalysis1[3].split("\t")
bad = imgAnalysis1[4].split("\t")
print(good,bad)
goodColors,badColors = 0,0
for i in range(5):
	goodColors += int(colors[i])
	badColors += int(colors[i+5])
goodColors = goodColors/5
badColors = badColors/5
f.close()
#[平均,the darkest,the lightest]

#----------print---------------

#輸入值
#y = ax+b
outColors = 0#之後要再改輸出
outLightDark = 0
#上升級數
def score(Min,Max,Input):
	a = 100/(Max-Min)
	x = Input - Min 
	print(a)
	if Input > Max:
		return 100-(((x*a)-100)/10)
	elif Input < Min:
		return x * a * -1 /10
	else:
		return x * a

outColors = score(badColors,goodColors,inputDemo.colors)
outLightDark = score(float(bad[0]),float(good[0]),inputDemo.difference)
print(outColors)
print(outLightDark)


#-----------------------分類圖片-----------------------

starColors = str(int(math.ceil(outColors/20)-1)) + "star"
starDarkLight = str(int(math.ceil(outLightDark/20)-1)) + "star"


cv2.imwrite("彩度/" + str(starColors) + "/" + str(inputDemo.pic),inputDemo.img,[cv2.IMWRITE_JPEG_QUALITY,50])
cv2.imwrite("對比/" + str(starDarkLight) + "/" + str(inputDemo.pic),inputDemo.img,[cv2.IMWRITE_JPEG_QUALITY,50])
