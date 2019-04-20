#讀取檔案(colors)
f = open("imgAnalysis.txt","r")
txt = f.readlines()
for i in range(len(txt)):
	txt[i] = txt[i].split("\t")
#print("txt的長度：%d" %len(txt))
total = []
lenght = len(txt)//2
for i in range(lenght):
	total.append(0)
	for j in range(len(txt[i])-1):
		total[i]+=int(txt[i][j])
#print("每一張圖片掃描之格數：",total)
colors = []
for i in range(lenght):
	colors.append(0)
	for j in range(len(txt[i])-1):
		if int(txt[i][j]) > total[i]//3000:
			colors[i] += 1
#print("每一張圖片總顏色數：",colors)
#讀取檔案(dark&light)
ugDifference,beauDifference = 0,0
ugDark,beauDark = 0,0
ugLight,beauLight = 0,0
badPhoto = []
goodPhoto = []
for i in range(len(txt)//2,(len(txt)//4)*3):
	beauDifference += abs(int(txt[i][0])-int(txt[i][1]))
	beauDark += int(txt[i][0])
	beauLight += int(txt[i][1])  
	goodPhoto.append((int(txt[i][0]),int(txt[i][1])))
for i in range((len(txt)//4)*3,len(txt)):
	ugDifference += abs(int(txt[i][0])-int(txt[i][1]))
	ugDark += int(txt[i][0])
	ugLight += int(txt[i][1])
	badPhoto.append((int(txt[i][0]),int(txt[i][1])))
f.close()

#---------------------------------分析數據------------------------------------

#分析 colors
mid = (len(colors)//2)
beauPhoto = 0
ugPhoto = 0
#print("中間值：%s"%mid)
for i in range(mid):
	beauPhoto+=colors[i]
beauPhoto = beauPhoto/mid
for i in range(mid,len(colors)):
	ugPhoto += colors[i]
ugPhoto = ugPhoto/mid
#print("好照片的平均顏色數是%s，差照片的平均顏色數是%s"%(beauPhoto,ugPhoto))

#分析 dark&light
ugDifference = ugDifference/5
ugLight = ugLight/5
ugDark = ugDark/5
beauDifference = beauDifference/5
beauLight = beauLight/5
beauDark = beauDark/5
print(colors)
print("goodPhoto:" , goodPhoto)
print("badPhoto:",badPhoto)
print("ug:平均差為%f，平均暗部為%f，平均亮部為%f"%(ugDifference,ugDark,ugLight))
print("beau:平均差為%f，平均暗部為%f，平均亮部為%f"%(beauDifference,beauDark,beauLight))

c = open("imgAnalysis1.txt","w+")
for i in range(10):
	c.write("%s\t"%colors[i])
c.write("\n")
newGoodPhoto,newBadPhoto = "",""
for i in range(5):
	for j in range(2):
		newBadPhoto += str(badPhoto[i][j]) + "\t"
		newGoodPhoto += str(goodPhoto[i][j]) + "\t"
	newBadPhoto += "|"
	newGoodPhoto+= "|"
c.write(newGoodPhoto+"\n")
c.write(newBadPhoto+"\n")
#c.write("\n%s\n"%str(goodPhoto))
#c.write("%s\n"%str(badPhoto))
c.write("%f\t%f\t%f\n"%(beauDifference,beauDark,beauLight))
c.write("%f\t%f\t%f\n"%(ugDifference,ugDark,ugLight))
c.close()