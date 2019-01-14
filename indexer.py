import re, sys, os

def lister(dir_name): #Lists all the files and folders in the current working directory
    for root, dirs, files in os.walk(dir_name, topdown=False):
        print(files)
        for name in files:
            print(name)
        for name in dirs:
            lister(name)

dir_name = input("Directory: ")
lister("\""+os.getcwd()+"/"+dir_name+"\"")