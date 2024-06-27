# A Depth First Search to traverse a tree and list down file names

from os import listdir
from os.path import isfile, join

def printnames(start_dir):
    print("\n Directory Name: ",start_dir)
    for file in sorted(listdir(start_dir)):
        filePath = join(start_dir, file)
        if isfile(filePath):
            print(file)
        else:
            printnames(filePath)


# printnames("searching")
printnames("../python")

# print(listdir("searching"))