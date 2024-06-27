from os import listdir
from os.path import isfile, join
from collections import deque

# A Breadth First Search to traverse a tree and list down file names
def printnames(start_dir):
    search_queue = deque()
    search_queue.append(start_dir)
    while search_queue:
        dir = search_queue.popleft()
        print("\n Directory Name: ",dir)
        for file in sorted(listdir(dir)):
            filePath = join(dir, file)
            if isfile(filePath):
                print("\n",file)
            else:
                search_queue.append(filePath)


printnames("searching")

# print(listdir("searching"))