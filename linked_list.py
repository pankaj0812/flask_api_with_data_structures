class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        list = []
        if self.head is None:
            return list

        node = self.head
        while node:
            list.append(node.data)
            node = node.next_node
        return list


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

    def insert_at_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node


# ll = LinkedList()
# ll.insert_beginning("data")
# ll.insert_beginning("data2")
# ll.insert_beginning("data3")
# ll.insert_at_end("data4")
# ll.insert_at_end("data5")
# ll.print_linkedlist()