class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None
        self.nodes_count = 0

    def is_list_empty(self):
        return self.head is None

    def get_nodes_count(self):
        return self.nodes_count

    def add_node_at_last_position(self, data):
        new_node = self.Node(data)
        if self.is_list_empty():
            self.head = new_node
            self.nodes_count += 1
        else:
            trav = self.head
            while trav.next is not None:
                trav = trav.next
            trav.next = new_node
            self.nodes_count += 1

    def add_node_at_first_position(self, data):
        new_node = self.Node(data)
        if self.is_list_empty():
            self.head = new_node
            self.nodes_count += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.nodes_count += 1

    def count_nodes(self):
        count = 0
        if not self.is_list_empty():
            trav = self.head
            while trav is not None:
                count += 1
                trav = trav.next
        return count

    def add_node_at_specific_position(self, pos, data):
        if pos == 1:
            self.add_node_at_first_position(data)
        elif pos == self.get_nodes_count() + 1:
            self.add_node_at_last_position(data)
        else:
            new_node = self.Node(data)
            i = 1
            trav = self.head
            while i < pos - 1:
                i += 1
                trav = trav.next
            new_node.next = trav.next
            trav.next = new_node
            self.nodes_count += 1

    def display_linked_list(self):
        if self.is_list_empty():
            raise RuntimeError("list is empty !!!")
        else:
            trav = self.head
            print("no. of nodes in a list are : ", self.get_nodes_count())
            print("list is : head -> ", end="")
            while trav is not None:
                print(trav.data, "-> ", end="")
                trav = trav.next
            print("null")

    def delete_node_at_first_position(self):
        if self.is_list_empty():
            raise RuntimeError("list is empty !!!")
        else:
            if self.head.next is None:
                self.head = None
                self.nodes_count -= 1
            else:
                self.head = self.head.next
                self.nodes_count -= 1

    def delete_node_at_last_position(self):
        if self.is_list_empty():
            raise RuntimeError("list is empty !!!")
        else:
            if self.head.next is None:
                self.head = None
                self.nodes_count -= 1
            else:
                trav = self.head
                while trav.next.next is not None:
                    trav = trav.next
                trav.next = None
                self.nodes_count -= 1

    def delete_node_at_specific_position(self, pos):
        if pos == 1:
            self.delete_node_at_first_position()
        elif pos == self.get_nodes_count():
            self.delete_node_at_last_position()
        else:
            i = 1
            trav = self.head
            while i < pos - 1:
                i += 1
                trav = trav.next
            trav.next = trav.next.next
            self.nodes_count -= 1

    def display_linked_list_in_reverse_order(self, trav):
        if trav is None:
            return
        self.display_linked_list_in_reverse_order(trav.next)
        print("{:4d}".format(trav.data), end="")

    def display_linked_list_in_reverse_order_wrapper(self):
        print("list in reverse order is : ")
        self.display_linked_list_in_reverse_order(self.head)
        print()

    def reverse_list(self):
        t1 = self.head
        t2 = t1.next
        t1.next = None

        while t2 is not None:
            t3 = t2.next
            t2.next = t1
            t1 = t2
            t2 = t3

        self.head = t1

    def search_node(self, data, temp):
        temp[0] = None
        trav = self.head
        while trav is not None:
            if data == trav.data:
                temp[1] = trav
                return True
            temp[0] = trav
            trav = trav.next

        temp[0] = None
        return False

    def search_and_delete(self, data):
        temp = [None, None]
        if not self.search_node(data, temp):
            return False

        cur = temp[1]
        prev = temp[0]

        if prev is None:
            print("node is found at first position => cur.data : {}".format(cur.data))
            self.head = cur.next
        else:
            print("prev.data : {}\t cur.data : {}".format(prev.data, cur.data))
            prev.next = cur.next

        self.nodes_count -= 1
        return True


def menu():
    print("***** Singly Linear Linked List Operations *****")
    print("0. Exit")
    print("1. Add node into the list at last position")
    print("2. Add node into the list at first position")
    print("3. Add node into the list at specific position")
    print("4. Delete node from the list at first position")
    print("5. Delete node from the list at last position")
    print("6. Delete node from the list at specific position")
    print("7. Display the list")
    print("8. Display the list in reverse order")
    print("9. Reverse list")
    print("10. Search and delete node from the list")
    choice = int(input("Enter the choice: "))
    return choice


if __name__ == "__main__":
    l1 = LinkedList()

    while True:
        choice = menu()
        if choice == 0:
            exit(0)
        elif choice == 1:
            data = int(input("Enter the data: "))
            l1.add_node_at_last_position(data)
        elif choice == 2:
            data = int(input("Enter the data: "))
            l1.add_node_at_first_position(data)
        elif choice == 3:
            while True:
                pos = int(input("Enter the position: "))
                if 0 < pos <= l1.get_nodes_count() + 1:
                    break
                print("Invalid position !!!")
            data = int(input("Enter the data: "))
            l1.add_node_at_specific_position(pos, data)
        elif choice == 4:
            try:
                l1.delete_node_at_first_position()
            except RuntimeError as e:
                print(e)
        elif choice == 5:
            try:
                l1.delete_node_at_last_position()
            except RuntimeError as e:
                print(e)
        elif choice == 6:
            while True:
                pos = int(input("Enter the position: "))
                if 0 < pos <= l1.get_nodes_count():
                    break
                print("Invalid position !!!")
            try:
                l1.delete_node_at_specific_position(pos)
            except RuntimeError as e:
                print(e)
        elif choice == 7:
            try:
                l1.display_linked_list()
            except RuntimeError as e:
                print(e)
        elif choice == 8:
            l1.display_linked_list_in_reverse_order_wrapper()
        elif choice == 9:
            l1.reverse_list()
        elif choice == 10:
            data = int(input("Enter the data to be deleted: "))
            l1.search_and_delete(data)
       
