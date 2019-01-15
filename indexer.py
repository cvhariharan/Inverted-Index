import re, sys, os, keywords_extractor
import json

def lister(dir_name): #Lists all the files and folders in the current working directory
    filesList = []
    for root, dirs, files in os.walk(dir_name, topdown=False):
        for name in files:
            filesList.append(name)
        for name in dirs:
            lister(name)
    return filesList

dir_name = input("Directory: ")
filesList = lister(os.getcwd()+"/"+dir_name)

index = {}
index["docslist"] = filesList
for eachFile in filesList:
    print(eachFile)
    f = open(dir_name+"/"+eachFile, encoding = "ISO-8859-1")
    text = f.read()
    f.close()
    extractor = keywords_extractor.Extractor(text)
    keywords = extractor.rank_words()
    print(keywords)
    for j in range(len(keywords)):
        if keywords[j] not in index.keys():
            index[keywords[j]] = []
        if eachFile not in index[keywords[j]]:
            index[keywords[j]].append(eachFile)
        index[keywords[j]].sort()

indexFile = open(os.getcwd()+"/index.json", "w")
indexFile.write(json.dumps(index))
indexFile.close()

