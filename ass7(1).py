class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None:
            print("The linked list is empty")
            return
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    def delete(self, data):
        if self.head is None:
            print("The linked list is empty")
            return
        if self.head.data == data:
            self.head = self.head.next
            print(f" {data} has been deleted")
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next is None:
            print(f"{data} not found.")
        else:
            current.next = current.next.next
            print(f"{data} has been deleted.")
ll = LinkedList()
while True:
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data to insert: "))
        ll.insert(data)
    elif choice == 2:
        data = int(input("Enter data to delete: "))
        ll.delete(data)
    elif choice == 3:
        ll.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
