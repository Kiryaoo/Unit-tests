import unittest
from ArrayList import ArrayList

class TestList(unittest.TestCase):
    def setUp(self):
        # Використовуємо змінну для вибору потрібної реалізації
        self.list = ArrayList()  # Можна змінити на CircularLinkedList для тесту іншої реалізації

    def test_append_and_length(self):
        self.assertEqual(self.list.length(), 0)
        self.list.append('a')
        self.list.append('b')
        self.assertEqual(self.list.length(), 2)

    def test_insert_and_get(self):
        self.list.append('a')
        self.list.append('c')
        self.list.insert('b', 1)
        self.assertEqual(self.list.get(0), 'a')
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.get(2), 'c')

    def test_delete(self):
        self.list.append('a')
        self.list.append('b')
        self.assertEqual(self.list.delete(0), 'a')
        self.assertEqual(self.list.length(), 1)

    def test_deleteAll(self):
        self.list.append('x')
        self.list.append('y')
        self.list.append('x')
        self.list.deleteAll('x')
        self.assertEqual(self.list.length(), 1)
        self.assertEqual(self.list.get(0), 'y')

    def test_clone_and_reverse(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('c')
        clone = self.list.clone()
        self.assertEqual(clone.length(), 3)
        self.list.reverse()
        self.assertEqual(self.list.get(0), 'c')
        self.assertEqual(self.list.get(1), 'b')
        self.assertEqual(self.list.get(2), 'a')

    def test_find(self):
        self.list.append('a')
        self.list.append('b')
        self.list.append('a')
        self.assertEqual(self.list.findFirst('a'), 0)
        self.assertEqual(self.list.findLast('a'), 2)
        self.assertEqual(self.list.findFirst('z'), -1)

    def test_clear(self):
        self.list.append('a')
        self.list.append('b')
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

def test_extend(self):
    self.list.append('a')
    other = ArrayList()
    other.append('b')
    other.append('c')
    self.list.extend(other._data) 
    self.assertEqual(self.list.length(), 3)
    self.assertEqual(self.list.get(2), 'c')

if __name__ == '__main__':
    unittest.main()
