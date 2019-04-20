
import _input_
gray = "i'm gray!!"
img = _input_.img
#黑白圖片
imgGray = _input_.imgGray
#長寬
width = imgGray.shape[1]
high = imgGray.shape[0]
#最亮和最暗
light = []
dark = []
lenght = width*high//40
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

#主程式，添加新的數值，再將最不亮（暗）的數值刪除
for i in range(0,len(imgGray),2):
	for j in range(0,len(imgGray[i]),2):
		find =imgGray[i][j]
		if find > light[0]:
			light.insert(binarySearch(light,find),find)
			light.pop(0)
		if find < dark[len(dark)-1]:
			dark.insert(binarySearch(dark,find),find)
			dark.pop(len(dark)-1)

print("最暗的10％的總數    "+str(len(dark)))
print("最亮的10％的總數    "+str(len(light)))
#計算平均值
darkTotal = 0
lightTotal = 0
for i in range(0,lenght):
	darkTotal += dark[i]
	lightTotal += light[i]
darkMean=darkTotal//lenght
lightMean=lightTotal//lenght
print("最暗的10％的平均值  "+str(darkMean))
print("最亮的10％的平均值  "+str(lightMean))

"""方案三：最舒服的圖片
	計算出圖片最亮的20％和最暗的20％的差距，不能相差太少（彩度低）。將照片裡面的極端值去除，再將中位數前後＿＿個值去除，剩下的兩半個算平均值，如果相差太多代表對比太大，顏色偏向兩極並不好看。
九宮格的中間那一格是否要加權，因為主體一般都在這個位置。
如果同類的顏色過多，也會降低分數
優：有創意、有突破性
缺：製作較為困難、需多方測試，測試出最完美的範例"""
