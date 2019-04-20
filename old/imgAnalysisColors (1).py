
import _input_
img = _input_.img
imgGray = _input_.imgGray
#rgb = [0,0,0]
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
print("色差分析")
print("↓↓↓↓↓↓20%↓↓↓↓↓↓↓40%↓↓↓↓↓↓↓60%↓↓↓↓↓↓↓80%↓↓↓↓↓↓↓100%")
for i in range(0,len(img),_input_.prec):
	for j in range(0,len(img[i]),_input_.prec):
		rgb[int(round((img[i][j][2])/64))][int(round((img[i][j][1])/64))][int(round((img[i][j][0])/64))]+=1
		st+=1
	if (50/len(img))*i>speed:
		print("#",end = "")
		speed+=1
#分析，儲存至big[]（可微調）	
#第零到二項為平均值以下（數量一定較多）
print("")	
print("掃描總數："+str(st))
#print(rgb)
big = [0,0,0,0,0,0,0,0]
whole = (len(img)//_input_.prec)*(len(img[0]//_input_.prec))
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
print(big)
#最後計分方式（可大改）
#如果大部分的顏色都趨於平均值，代表彩度不高，分數會降低
score = big[0]-big[2]-big[3]
print("Score:"+str(score))











#建立rgb的三維陣列(空值)
#方案三
'''for r in range(16):
	rgb.append([])
	for g in range(16):
		rgb[r].append([])
		for b in range(16):
			rgb[r][g].append(0)'''
#方案一、二
'''red,green,blue = 0,0,0
for col in range(0,len(img),_input_.prec):
	for row in range(0,len(img[col]),_input_.prec):
		#方案一
		red+= img[col][row][2]
		green+= img[col][row][1]
		blue+= img[col][row][0]
		#方案二
		if red>green and red>blue:
			rgb[0] +=1
		elif green>red and green>blue:
			rgb[1] +=1
		else:
			rgb[2] += 1
print(rgb)
rgb = list(map(lambda x:x//(col*row),rgb))
print(rgb)
print(red,green,blue)

red = red//(col*row)
green = green//(col*row)
blue = blue//(col*row)
print(red,green,blue)
'''
#方案三
'''
將256個顏色簡化成16個階層，輸入rgb各個顏色的量
for col in range(0,len(img),_input_.prec):
	for row in range(0,len(img[col]),_input_.prec):
		rgb[(img[col][row][0])//16][(img[col][row][1])//16][(img[col][row][2])//16]+=1
print(rgb)
'''
#red
#green
#blue
