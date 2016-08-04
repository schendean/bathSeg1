import numpy as np
import Image
import os


fileIndex = 0
fread = open('data.txt','r')
fwrite = open('123.txt','w')
fwriteDoc = open('ADocList.txt','w')
documents = fread.readlines()

listDoc = [];
listDocName = [];

for line in documents:
    sp = line.split('/')
    if not (sp[0] in listDoc):
	fwrite.close()
	fwrite = open(sp[0]+'.txt','w')
	listDoc.append(sp[0])
	fwriteDoc.write(sp[0]+'\n')
    fwrite.write(sp[1])



print len(listDoc)






	




