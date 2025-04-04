class Node:
    def __init__(self, value: str):
        self.value = value
        self.next = None


class ArrayList:
    def __init__(self):
        self.head = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def append(self, element: str) -> None:
        new_node = Node(element)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        new_node = Node(element)
        if index == 0:
            if not self.head:
                self.head = new_node
                new_node.next = new_node
            else:
                tail = self.head
                while tail.next != self.head:
                    tail = tail.next
                new_node.next = self.head
                self.head = new_node
                tail.next = self.head
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if self.size == 1:
            value = self.head.value
            self.head = None
        elif index == 0:
            value = self.head.value
            tail = self.head
            while tail.next != self.head:
                tail = tail.next
            self.head = self.head.next
            tail.next = self.head
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            value = prev.next.value
            prev.next = prev.next.next
        self.size -= 1
        return value

    def deleteAll(self, element: str) -> None:
        index = 0
        current = self.head
        for _ in range(self.size):
            if current.value == element:
                self.delete(index)
                current = self.head
                index = 0
                continue
            current = current.next
            index += 1

    def get(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        current = self.head
        for _ in range(index):
            current = current.next
        return current.value

    def clone(self) -> "ArrayList":
        clone_list = ArrayList()
        current = self.head
        for _ in range(self.size):
            clone_list.append(current.value)
            current = current.next
        return clone_list

    def reverse(self) -> None:
        if not self.head or self.size == 1:
            return
        prev = None
        current = self.head
        tail = self.head
        for _ in range(self.size):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head.next = prev
        self.head = prev
        while tail.next != prev:
            tail = tail.next
        tail.next = self.head

    def findFirst(self, element: str) -> int:
        current = self.head
        for i in range(self.size):
            if current.value == element:
                return i
            current = current.next
        return -1

    def findLast(self, element: str) -> int:
        current = self.head
        last_index = -1
        for i in range(self.size):
            if current.value == element:
                last_index = i
            current = current.next
        return last_index

    def clear(self) -> None:
        self.head = None
        self.size = 0

    def extend(self, elements: list) -> None:
        for el in elements:
            self.append(el)
