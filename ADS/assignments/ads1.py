class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at the end
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Display the list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    # Split into two equal queues
    def split_queue(self):
        if self.head is None:
            return None, None

        # Find middle using slow & fast pointers
        slow = self.head
        fast = self.head

        while fast and fast.next:
            fast = fast.next.next
            if fast:
                slow = slow.next

        # Create second queue
        second = DoublyLinkedList()
        second.head = slow.next

        if second.head:
            second.head.prev = None

        second.tail = self.tail

        # Create first queue
        first = DoublyLinkedList()
        first.head = self.head
        first.tail = slow

        slow.next = None
        self.tail = slow

        return first, second


#implementation

queue = DoublyLinkedList()

people = int(input("Enter number of people: "))

for i in range(people):
    name = input(f"Person {i+1}: ")
    queue.insert_end(name)

print("\nOriginal Queue:")
queue.display()

stall1, stall2 = queue.split_queue()

print("\nStall 1 Queue:")
stall1.display()

print("Stall 2 Queue:")
stall2.display()