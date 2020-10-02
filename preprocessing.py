import os 
from xml.dom import minidom
import xlsxwriter
location = os.getcwd() 
counter = 0 
trainfiles = [] 
otherfiles = [] 

print(location)
workbook = xlsxwriter.Workbook('datatrainpre.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:A',20)

for file in os.listdir(location):
    try:
        if file.endswith(".xml"):
            #print "txt file found:\t", file
            trainfiles.append(str(file))
            counter = counter+1
        else:
            otherfiles.append(file)
            counter = counter+1
    except Exception as e:
        raise e
        print "No files found here!"
   
count = 0
worksheet.write(0,0,'Berita')
worksheet.write(0,1,'File')

trainfiles.sort()
for i in trainfiles:
	print(i)
for xmlfile in trainfiles:
	xmldoc = minidom.parse(xmlfile)
	p = xmldoc.getElementsByTagName("p")[1]
	par = xmldoc.getElementsByTagName("p")
	paragraph = " "
	for i in range(0,len(par)):
		p = xmldoc.getElementsByTagName("p")[i]
		paragraph += p.childNodes[0].data
		worksheet.write(count+1,0,paragraph)
		worksheet.write(count+1,1,str(trainfiles[count]).replace('.xml',''))
		#print(p.childNodes[0].data)
	#print("Isi tag : ",p.childNodes[0].data)
	count +=1
	

print "Total files found:\t", counter

workbook.close()
