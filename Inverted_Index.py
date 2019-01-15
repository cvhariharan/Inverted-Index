#Construct an Inverted Index for a given document collection comprising of at least 50 documents with a total vocabulary size of at least 1000 words.

#import the documents (we have the news folder)

#tokenize them(we have the keywords_extractor)

#linguistic module(we have the keywords_extractor)

#create the inverted index

import keywords_extractor

Index={}
for i in range(487)[1:]:
	if(int(i/100)!=0):
		fileName="0"+str(i)
	elif(int(i/10)!=0):
		fileName="00"+str(i)
	else:
		fileName="000"+str(i)
	print(fileName)
	f=open("./News/"+fileName, encoding = "ISO-8859-1")
	text=f.read()
	extractor = keywords_extractor.Extractor(text)
	tempIndex=(extractor.rank_words())
	for i in tempIndex:
		if i in Index.keys():
			print("Hii"+i)
			Index[i][0]+=1
			Index[i].append(fileName)
		else:
			Index[i]=[1,fileName]
	print(Index)


