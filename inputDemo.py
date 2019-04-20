import numpy as np
import cv2
#-------------------input--------------------------------


pic = input("輸入圖片檔名(僅支援.jpg，不須加副檔名):") +".jpg"
#引進圖片檔
img = cv2.imread(pic)
imgGray = cv2.imread(pic, cv2.IMREAD_GRAYSCALE)
print(img.shape)
if img.shape[0]*img.shape[1] < 360000:
	prec = 1
elif img.shape[0]*img.shape[1] < 640000:
	prec = 2
elif img.shape[0]*img.shape[1] < 1000000:
	prec = 3
else:
	prec = 4
pers = 10


#-----------------imgAnalysisGray------------------------------


#長寬
width = imgGray.shape[1]
high = imgGray.shape[0]
#最亮和最暗
light = []
dark = []
lenght = width*high//((prec*prec)*pers)
for i in range(0,lenght):
	dark.append(256)
	light.append(-1)
#二分搜尋法
def  binarySearch(a,Find):
	low = 0
	high = len(a) - 1
	while low <= high:
	    mid = (low + high) // 2
	    if a[mid] > Find:
	        high = mid - 1
	    elif a[mid] < Find:
	        low = mid + 1
	    else:
	        break
	return mid
#記錄速度
speed = 0
print("")
print("亮度分析")
print("↓↓↓↓↓↓20%↓↓↓↓↓↓↓40%↓↓↓↓↓↓↓60%↓↓↓↓↓↓↓80%↓↓↓↓↓↓↓100%")
#主程式，添加新的數值，再將最不亮（暗）的數值刪除
for i in range(0,high,prec):
	for j in range(0,width,prec):
		find =imgGray[i][j]
		if find > light[0]:
			light.insert(binarySearch(light,find),find)
			light.pop(0)
		if find < dark[len(dark)-1]:
			dark.insert(binarySearch(dark,find),find)
			dark.pop(len(dark)-1)
	if (50/high)*i>speed:
		print("#",end = "")
		speed+=1
print("\n")
#		print("最暗的10％的總數    "+str(len(dark)))
#		print("最亮的10％的總數    "+str(len(light)))
#計算平均值
darkTotal = 0
lightTotal = 0
for i in range(0,lenght):
	darkTotal += dark[i]
	lightTotal += light[i]
darkMean=darkTotal//lenght
lightMean=lightTotal//lenght
print("最暗的的平均值  "+str(darkMean))
print("最亮的的平均值  "+str(lightMean))
#		print("")
difference = lightMean-darkMean


#--------------------imgAnalysisColors-----------------------


#建立空殼陣列
rgb = []
for a in range(5):
	rgb.append([])
	for b in range(5):
		rgb[a].append([])
		for c in range(5):
			rgb[a][b].append(0)
#主程式，利用四捨五入將所有顏色分配到5x5x5的陣列裡，紀錄每一格的數量
speed = 0
st = 0
print("主體色分析")
print("↓↓↓↓↓↓20%↓↓↓↓↓↓↓40%↓↓↓↓↓↓↓60%↓↓↓↓↓↓↓80%↓↓↓↓↓↓↓100%")
for i in range(0,len(img),prec):
	for j in range(0,len(img[i]),prec):
		rgb[int(round((img[i][j][2])/64))][int(round((img[i][j][1])/64))][int(round((img[i][j][0])/64))]+=1
		st+=1
	if (50/len(img))*i>speed:
		print("#",end = "")
		speed+=1
total = len(img)*len(img[0])/(prec**2)
colors = 0
for r in range(5):
	for g in range(5):
		for b in range(5):
			if rgb[r][g][b] > total//3000:
				colors += 1
print(difference)
print(colors)