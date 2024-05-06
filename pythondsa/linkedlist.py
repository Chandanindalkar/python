class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        # indicating the LL is empty
        self.head = None

    # operations
    def print_LL(self):
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n is not None:
                print(n.data, "-->", end=" ")
                n = n.ref
            print("\n")

    def add_empty(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print('the list is not empty')

    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Linked List is empty!")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return

        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print("node is not present in list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def pop(self):  # delete first node
        if self.head is None:
            print('the list is empty')
        else:
            self.head = self.head.ref

    def del_end(self):
        n = self.head
        if n is None:
            print('the list is empty')
        elif self.head.ref is None:
            self.head = None
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None

    def delete(self, x):

        if self.head is None:
            print('list is empty')

        elif self.head.data == x:
            self.head = self.head.ref

        n = self.head
        while n.ref is not None:
            if x == n.ref.data:
                break
            n = n.ref
        if n.ref is None:
            print('node is not present')
        else:
            n.ref = n.ref.ref


ll1 = LinkedList()
ll1.print_LL()

ll1.add_empty(10)
ll1.print_LL()

ll1.add_begin(20)
ll1.print_LL()

ll1.add_begin(30)
ll1.print_LL()

ll1.add_end(101)
ll1.print_LL()

ll1.add_after(500, 10)
ll1.print_LL()

ll1.add_before(6969, 500)
ll1.print_LL()

ll1.pop()
ll1.print_LL()

ll1.del_end()
ll1.print_LL()

ll1.delete(6969)
ll1.print_LL()