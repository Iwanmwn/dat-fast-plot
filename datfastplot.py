import matplotlib.pyplot as plt

datfilename = "f1.dat"

arr = list()
with open(datfilename) as file:
    content = file.readlines()
    for line in content:
        arr.append(line[:-1].split('	'))

plt.plot(arr)
plt.ylabel('Coordinate Y')
plt.xlabel('Coordinate X')

plt.legend(['1', '2', '3', '4', '5', '6', '7'], loc = 'upper right')

plt.show()
