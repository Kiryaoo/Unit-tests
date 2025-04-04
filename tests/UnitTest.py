import unittest
from ArrayList import ArrayList

class TestArrayList(unittest.TestCase):
    def setUp(self):
        self.list = ArrayList()

    def test_append(self):
        self.list.append('a')
        self.assertEqual(self.list.length(), 1)

    def test_insert(self):
        self.list.append('a')
        self.list.insert('b', 1)
        self.assertEqual(self.list.get(1), 'b')
        with self.assertRaises(IndexError):
            self.list.insert('c', 5)

    def test_delete(self):
        self.list.append('a')
        self.list.append('b')
        self.assertEqual(self.list.delete(0), 'a')
        with self.assertRaises(IndexError):
            self.list.delete(2)

    def test_deleteAll(self):
        self.list.extend(['a', 'b', 'a', 'c'])
        self.list.deleteAll('a')
        self.assertEqual(self.list._data, ['b', 'c'])

    def test_get(self):
        self.list.append('x')
        self.assertEqual(self.list.get(0), 'x')
        with self.assertRaises(IndexError):
            self.list.get(5)

    def test_clone(self):
        self.list.append('a')
        cloned = self.list.clone()
        self.assertEqual(cloned.get(0), 'a')
        cloned.append('b')
        self.assertNotEqual(self.list.length(), cloned.length())

    def test_reverse(self):
        self.list.extend(['a', 'b', 'c'])
        self.list.reverse()
        self.assertEqual(self.list._data, ['c', 'b', 'a'])

    def test_findFirst(self):
        self.list.extend(['a', 'b', 'a'])
        self.assertEqual(self.list.findFirst('a'), 0)
        self.assertEqual(self.list.findFirst('z'), -1)

    def test_findLast(self):
        self.list.extend(['a', 'b', 'a'])
        self.assertEqual(self.list.findLast('a'), 2)
        self.assertEqual(self.list.findLast('z'), -1)

    def test_clear(self):
        self.list.append('x')
        self.list.clear()
        self.assertEqual(self.list.length(), 0)

    def test_extend(self):
        self.list.append('x')
        self.list.extend(['y', 'z'])
        self.assertEqual(self.list._data, ['x', 'y', 'z'])

if __name__ == "__main__":
    unittest.main()