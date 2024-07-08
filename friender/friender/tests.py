import unittest
from .unique_queue import UniqueQueue

class TestUniqueQueue(unittest.TestCase):
    def test_add_unique_elements(self):
        q = UniqueQueue()
        q.add(1)
        q.add("hello")
        q.add([1, 2, 3])
        self.assertEqual(q.length(), 3)

    def test_add_duplicates(self):
        q = UniqueQueue()
        q.add(1)
        q.add(1)
        self.assertEqual(q.length(), 1)

    def test_empty_queue(self):
        q = UniqueQueue()
        self.assertEqual(q.length(), 0)

    def test_last_added_element(self):
        q = UniqueQueue()
        q.add(1)
        q.add(2)
        self.assertEqual(q.last_added(), 2)

    def test_remove_element(self):
        q = UniqueQueue()
        q.add(1)
        q.add(2)
        q.add(3)
        q.data.remove(2)
        self.assertNotIn(2, q.data)

    def test_check_element_presence(self):
        q = UniqueQueue()
        q.add(1)
        self.assertTrue(1 in q.data)
        self.assertFalse(2 in q.data)

    def test_length_after_removal(self):
        q = UniqueQueue()
        q.add(1)
        q.add(2)
        q.add(3)
        q.data.remove(2)
        self.assertEqual(q.length(), 2)

    def test_different_data_types(self):
        q = UniqueQueue()
        q.add(1)
        q.add("hello")
        q.add([1, 2, 3])
        self.assertEqual(q.length(), 3)

    def test_empty_queue_last_added(self):
        q = UniqueQueue()
        self.assertIsNone(q.last_added())

    def test_large_data_volume(self):
        q = UniqueQueue()
        for i in range(10000):
            q.add(i)
        self.assertEqual(q.length(), 10000)