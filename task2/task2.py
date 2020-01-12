import sys

data1 = []
data2 = []
data3 = []
data4 = []
data5 = []
data6 = []
sums=0
def liniya(x,y,x1,y1,x2,y2):
    if((x-x1)*(y2-y1)-(y-y1)*(x2-x1)<=0)and((x1<x<x2 or x2<x<x1 or y1<y<y2 or y2<y<y1)):
        return(1) 
with open(sys.argv[1]) as f:
    for line in f:
        a,b=map(float,line.split())
        data1.append(float(a))
        data2.append(float(b))
with open(sys.argv[2]) as f:
    for line in f:
        a,b=map(float,line.split())
        data3.append(float(a))
        data4.append(float(b))
print(data1,data2)
data5=data1.copy()
data6=data2.copy()
data5.append(float(data5[0]))
data6.append(float(data6[0]))
print(data5,data6)
for i in range(len(data3)):
    c=0
    sums=0
    for z in range (len(data1)):
        sums=0
        if data1[z]==data3[i] and data2[z]==data4[i]:
            sums+=1
            print(0)
            break
        elif liniya(data3[i],data4[i],data5[z],data6[z],data5[z+1],data6[z+1])==1:
            sums+=1
            print(1)
            break
        elif (((data2[z]<=data4[i] and data4[i]<data2[z-1]) or (data2[z-1]<=data4[i] and data4[i]<data2[z])) and \
            (data3[i] > (data1[z-1] - data1[z]) * (data4[i] - data2[z]) / (data2[z-1] - data2[z]) + data1[z])):
            print(2)
            sums+=1
            break
    if sums==0:
        print(3)
