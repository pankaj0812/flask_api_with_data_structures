class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None


    def print_linkedlist(self):
        linkedlist_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            linkedlist_string += f" {str(node.data)} ->"
            node = node.next_node
        
        linkedlist_string += " None"
        print(linkedlist_string)

ll = LinkedList()
node4 = Node("data4", None)
node3 = Node("data3", node4)
node2 = Node("data2", node3)
node1 = Node("data1", node2)

ll.head = node1
ll.print_linkedlist()