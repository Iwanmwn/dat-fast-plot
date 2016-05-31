import numpy as np
import matplotlib.pyplot as plt

datfilename = "f1.dat"

datfile = open(datfilename)

rows = 0
cols = 0
for i, l in enumerate(datfile):
	rows += 1
	if(i == 0):
		for j in range(0, len(l)):
			if(l[j] + l[j - 1] == "  " or l[j] == "\t"):
				cols += 1
print("rows: ", rows, "; cols: ", cols)
arr = np.zeros((rows, cols + 1), dtype = float)

datfile = open(datfilename)

for i, l in enumerate(datfile):
	num = 0
	tempStr = ""
	for j in range(0, len(l)):
		if( l[j] == "1" or l[j] == "2" or l[j] == "3" or l[j] == "4" or l[j] == "5" or l[j] == "6" or l[j] == "7" or l[j] == "8" or l[j] == "9" or l[j] == "0" or l[j] == "." ):
			tempStr += l[j]
		elif(len(tempStr) > 0):
			#print(tempStr)
			arr[i][num] = tempStr
			num += 1
			tempStr = ""

#print(arr[3][1])

plt.plot(arr)
plt.ylabel('Coordinate Y')
plt.xlabel('Coordinate X')

plt.legend(['1', '2', '3', '4', '5', '6', '7'], loc = 'upper right')

plt.show()