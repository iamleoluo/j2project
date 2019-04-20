import numpy as np
import cv2
#導入txt檔
r = open('imgAnalysis.txt', 'w+')
#宣告變數
File = []
file = 1
photo = 10
for file in range(file):
	#File.append([])
	for photo in range(photo):
		print("\n"+str(file)+"-"+str(photo)+"\n")
		#-------------------input--------------------------------


		pic = "pictures/mount" + str(photo) +".jpg"
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
		print("")
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
#		print("最暗的"+str(pers)+"％的平均值  "+str(darkMean))
#		print("最亮的"+str(pers)+"％的平均值  "+str(lightMean))
#		print("")


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
		#分析，儲存至big[]（可微調）	
		#第零到二項為平均值以下（數量一定較多）
#		print("")	
#		print("掃描總數："+str(st))
		#print(rgb)
		big = [0,0,0,0,0,0,0,0]
		whole = (len(img)//prec)*(len(img[0]//prec))
		for a in range(5):
			for b in range(5):
				for c in range(5):
					if rgb[a][b][c] > st//300:
						if rgb[a][b][c] > st//200:
							if rgb[a][b][c] > st//125:
								if rgb[a][b][c] > st//100:
									if rgb[a][b][c] > st//50:
										if rgb[a][b][c] > st//25:
											big[6]+=1
										else:
											big[5]+=1
									else:
										big[4]+=1
								else:
									big[3]+=1
							else:
								big[2]+=1
						else:
							big[1]+=1
					else:
						big[0]+=1
#		print(big)
		#最後計分方式（可大改）
		#如果大部分的顏色都趨於平均值，代表主體不明顯，分數會降低
		score = big[0]-big[2]-big[3]
#		print("Score:"+str(score))

		#--------------------output--------------------------------
		File.append([darkMean,lightMean,big,score])
		for R in range(5):
			for G in range(5):
				for B in range(5):
					r.write(str(rgb[R][G][B])+"\t")
		r.write("\n")
print("\n")
print(File)
for i in range(photo+1):
	for j in range(2):
		print(File[i][j],end = " ")
		r.write(str(File[i][j])+"\t")
	print("")
	r.write("\n")

r.close()
'''for i in range(5):
	if File[i][0][1] - File[i][0][0] + File[i][0][3]<File[i][1][1] - File[i][1][0] + File[i][1][3]:
		print(str(i)+"."+"1.jpg")
	else:
		print(str(i)+"."+"0.jpg")'''

'''
		#輸出圖片cv2.imwrite(檔名,陣列,參數(品質0~100))
		cv2.imwrite('output.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,100])

		#輸出圖片cv2.imwrite(檔名,陣列,參數(png壓縮層級0~9))
		cv2.imwrite('output.png',img,[cv2.IMWRITE_PNG_COMPRESSION,9])

		cv2.imwrite('outputGray.jpg',imgGray)'''
