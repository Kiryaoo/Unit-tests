class ArrayList:
    def __init__(self):
        self._data = []

    def length(self) -> int:
        return len(self._data)

    def append(self, element: str) -> None:
        self._data.append(element)

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > len(self._data):
            raise IndexError("Index out of bounds")
        self._data.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data.pop(index)

    def deleteAll(self, element: str) -> None:
        self._data = [e for e in self._data if e != element]

    def get(self, index: int) -> str:
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of bounds")
        return self._data[index]

    def clone(self) -> "ArrayList":
        cloned_list = ArrayList()
        cloned_list.extend(self._data)
        return cloned_list

    def reverse(self) -> None:
        self._data.reverse()

    def findFirst(self, element: str) -> int:
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        try:
            return len(self._data) - 1 - self._data[::-1].index(element)
        except ValueError:
            return -1

    def clear(self) -> None:
        self._data.clear()

    def extend(self, elements: list) -> None:
        self._data.extend(elements)