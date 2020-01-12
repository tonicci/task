import numpy
import sys

def toFixed(numObj, digits=2):
    return f"{numObj:.{digits}f}"

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return int(sortedLst[index] + sortedLst[index + 1])/2
    
data = []
with open(sys.argv[1]) as f:
    for line in f:
        data.append(float(line))
print(toFixed(numpy.percentile(data,90)))
print(toFixed(median(data)))
print(toFixed(max(data)))
print(toFixed(min(data)))
print(toFixed(numpy.mean(data)))
