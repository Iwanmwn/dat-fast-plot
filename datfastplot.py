import matplotlib.pyplot as plt

plt.plot([line.split() for line in open("f1.dat")])
plt.ylabel('Coordinate Y')
plt.xlabel('Coordinate X')
plt.legend(range(1, 7), loc='upper right')
plt.show()
