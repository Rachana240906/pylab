class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, data):
        self.queue.append(data)
    def dequeue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            return self.queue.pop(0)
    def display(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print("Queue:", "  ".join(map(str, self.queue)))
queue = Queue()
while True:
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter data : "))
        queue.enqueue(data)
    elif choice == 2:
        result = queue.dequeue()
        if result is not None:
            print(f"Dequeued: {result}")
    elif choice == 3:
        queue.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
