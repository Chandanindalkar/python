from collections import deque

# Implement BFS to find mango seller in the graph
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = ["you"] # peggy is friends with "you", might cause infi-loop
graph["thom"] = []
graph["jonny"] = []

searched_queue = set()
search_queue = deque()

# First degree
search_queue += graph["you"]
searched_queue.add("you")

def mangoSeller(name):
    return True if name[-1] == 'm' else False

while search_queue:
    person = search_queue.popleft()
    if (person not in searched_queue):
        if mangoSeller(person):
            print('The Mango Seller is: ', person)
        else:
            search_queue += graph[person]
            searched_queue.add(person)

# print(search_queue)