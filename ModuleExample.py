import Circle
import ReverseName

def ModulePractice():
    print('Example of implementing modules of another files in current file')
    Circle.area()                   #This is for importing area module of Circle file
    ReverseName.reverse()           #importing reverse module of ReverseName file
    CurrentFile()                   #module of current file
    Circle.CommonFunction()         #Module of Circle file, same named module available in ReverseName file
    ReverseName.CommonFunction()    #Reversename file's module

def CurrentFile():
    print('Hello, you are running method of current file')

def main():
    ModulePractice()

main()



