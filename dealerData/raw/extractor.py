import os
import csv

headers = ['sno', 'name', 'address', 'locality', 'city', 'state', 'pincode', 'type', 'phone1', 'phone2', 'mobile' ]

def readFile(filename):
    try:
        with open(filename, mode='r') as file:
            fileContent = csv.reader(file)
            return fileContent
    except:
        print("someting has gone wrong!!")

def getFileInput():
    filename = input("enter file to extract: ")
    files = os.listdir()
    if filename in files:
        return filename
    else:
        print("file does not exist try again \n")
        getFileInput()


def packageData(headers, dataRow):
    pass


