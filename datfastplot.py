import matplotlib.pyplot as plt

datfilename = "f1.dat"

plt.plot([line.split() for line in open(datfilename)])
plt.ylabel('Coordinate Y')
plt.xlabel('Coordinate X')

plt.legend(['1', '2', '3', '4', '5', '6', '7'], loc = 'upper right')

plt.show()
