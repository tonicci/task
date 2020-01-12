import sys
data = []
data1 = []
data2 = []
data3 = []
data4 = []
data5 = []

with open(sys.argv[1]+"\\Cash1.txt") as f:
    for line in f:
        data1.append(float(line))

with open(sys.argv[1]+"\\Cash2.txt") as f:
    for line in f:
        data2.append(float(line))

with open(sys.argv[1]+"\\Cash3.txt") as f:
    for line in f:
        data3.append(float(line))

with open(sys.argv[1]+"\\Cash4.txt") as f:
    for line in f:
        data4.append(float(line))

with open(sys.argv[1]+"\\Cash5.txt") as f:
    for line in f:
        data5.append(float(line))

for i in range (len(data1)):
    data.append(float(data1[i]+data2[i]+data3[i]+data4[i]+data5[i]))
print(data.index(max(data))+1)
