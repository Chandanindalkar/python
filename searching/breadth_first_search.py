from collections import deque

# Implement BFS to find mango seller in the graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

search_queue = deque()

# First degree
search_queue += graph["you"]

def mangoSeller(name):
    return True if name[-1] == 'm' else False

while search_queue:
    person = search_queue.pop()
    if mangoSeller(person):
        print('The Mango Seller is: ', person)
    else:
        search_queue += graph[person]

# print(search_queue)