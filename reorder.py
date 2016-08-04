import numpy as np
import Image
import os

def merge(list1,list2):
    listMerged = []
    print str(len(list1))+','+str(len(list2))
    while len(list1)>0 and len(list2)>0:
	if list1[0]<list2[0]:
	    listMerged.append(list1[0])
	    list1 = list1[1:]
	else:
	    listMerged.append(list2[0])
	    list2 = list2[1:]
    print 'len:'+str(len(listMerged+list1+list2))
    return listMerged+list1+list2

def recursive(listU,length):
    print length
    if length==0:
	print 'error'
    elif length==1:
        return [listU[0]]
    elif length>2:
	indmid = length/2
	list1 = recursive(listU[0:indmid],indmid)
	list2 = recursive(listU[indmid:length],length-indmid)
    else:
	list1 = [listU[0]]
	list2 = [listU[1]]
    return merge(list1,list2)

fileIndex = 0
fread = open('directory.txt','r')
fwrite = open('data.txt','w')


gather=[0]*65239
count=[0]*65239
encoding=[0]*65239


documents = fread.readlines()
numFile = len(documents)
print numFile

newList = recursive(documents,numFile)

print len(newList)


for li in newList:
    fwrite.write(li)
    print li

print 'all'






	




