import sys

data1=[]
data2=[]
data3=[]
data4=[]
data5=[]
data6=[]
data7=[]
sums=0
s=0
q=0
d=0

with open(sys.argv[1]) as f:
    i=0
    for line in f:  
        a,b=(line.split())
        a,c=map(int,a.split(':'))
        b,d=map(int,b.split(':'))
        data1.append(int(a))
        data2.append(int(c))
        data3.append(int(b))
        data4.append(int(d))
        data5.append(int(a*100+c))
        data6.append(int(b*100+d))
        data7.append(int(a*100+c))
        data7.append(int(b*100+d))
data7=sorted(data7)
data=[0]*len(data7)

for i in range (len(data7)):
    for z in range(len(data2)):
        if (data7[i]>=data5[z] and data7[i]<data6[z]) or (data7[i]>=data5[z] and data7[i]<data6[z]):
            data[i]+=1
for i in range (len(data)):
    if (data[i]==max(data) and i==0) or (data[i]==max(data) and data[i-1]!=max(data)):
        sums+=1
        q=data7[i]
    if (data[i]==max(data) and i==len(data)) or (data[i]==max(data) and data[i+1]!=max(data)):
        s+=1
        d=data7[i+1]
    if sums==1 and s==1:
        if d%100//10==0:
            print(q//100,":",q%100," ",d//100,":",0,d%100,sep = '')
        else:
            print(q//100,":",q%100," ",d//100,":",d%100,sep='')
        sums=0
        s=0

    

