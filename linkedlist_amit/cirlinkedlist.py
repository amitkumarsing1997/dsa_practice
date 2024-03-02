class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.nodesCount = 0

    def is_list_empty(self):
        return self.head is None

    def get_nodes_count(self):
        return self.nodesCount

    def add_node_at_last_position(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.nodesCount += 1
        else:
            trav = self.head
            while trav.next != self.head:
                trav = trav.next
            trav.next = new_node
            new_node.next = self.head
            self.nodesCount += 1

    def add_node_at_first_position(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            self.nodesCount += 1
        else:
            trav = self.head
            while trav.next != self.head:
                trav = trav.next
            new_node.next = self.head
            self.head = new_node
            trav.next = self.head
            self.nodesCount += 1

    def display_linked_list(self):
        if not self.is_list_empty():
            trav = self.head
            print("list is:", end=" ")
            while True:
                print(f"{trav.data:4}", end="")
                trav = trav.next
                if trav == self.head:
                    break
            print()
            print("no. of nodes in a list are:", self.get_nodes_count())
        else:
            print("list is empty !!!")

    def delete_node_at_first_position(self):
        if not self.is_list_empty():
            if self.head == self.head.next:
                self.head = None
                self.nodesCount -= 1
            else:
                trav = self.head
                while trav.next != self.head:
                    trav = trav.next
                self.head = self.head.next
                trav.next = self.head
                self.nodesCount -= 1


if __name__ == "__main__":
    l1 = LinkedList()

    l1.add_node_at_last_position(11)
    l1.add_node_at_last_position(22)
    l1.add_node_at_last_position(33)
    l1.add_node_at_last_position(44)
    l1.add_node_at_last_position(55)

    l1.display_linked_list()

    # l1.add_node_at_first_position(99)
    l1.delete_node_at_first_position()

    l1.display_linked_list()
