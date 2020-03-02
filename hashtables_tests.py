import unittest

from hashtables import HashTableSepchain, HashTableLinear, HashTableQuadratic
from hashtables import hash_string, import_stopwords, enlarge

class MyTest(unittest.TestCase):
    # hash of 'us' is 2
    def test_HashTableSepChain(self):
        t = HashTableSepchain()
        print(t)
        print(type(t))
        self.assertEqual(t.size(), 0)
        t.put('us', 'us')
        print(type(t[2]))
        print(t[2])
        self.assertEqual(t[2].key, 'us')
    #     self.assertTrue(pq.is_empty())
    #     for i in reversed(range(5)):
    #         print("pq.insert(", i, ")")
    #         pq.insert(i)
    #     self.assertEqual(pq.size(), 5)
    #     self.assertFalse(pq.is_empty())
    #     self.assertEqual(pq.min(), 0)
    #
    # def test_pq2(self):
    #     pq = MinPQ()
    #     self.assertTrue(pq.is_empty())
    #     for i in reversed(range(5)):
    #         print("pq.insert(", i, ")")
    #         pq.insert(i)
    #     self.assertEqual(pq.size(), 5)
    #     self.assertFalse(pq.is_empty())
    #     self.assertEqual(pq.min(), 0)
    #     self.assertEqual(pq.del_min(), 0)
    #     self.assertEqual(pq.del_min(), 1)
    #     self.assertEqual(pq.del_min(), 2)
    #     self.assertEqual(pq.del_min(), 3)
    #     self.assertEqual(pq.del_min(), 4)
    #     self.assertTrue(pq.is_empty())
    #     self.assertEqual(pq.size(), 0)
    #
    # def test_pq3(self):
    #     pq = MinPQ()
    #     self.assertTrue(pq.is_empty())
    #     i = 1
    #     print("pq.insert(", i, ")")
    #     pq.insert(i)
    #     self.assertEqual(pq.min(), 1)
    #     i = 5
    #     print("pq.insert(", i, ")")
    #     pq.insert(i)
    #     self.assertEqual(pq.min(), 1)
    #     i = 3
    #     print("pq.insert(", i, ")")
    #     pq.insert(i)
    #     self.assertEqual(pq.del_min(), 1)
    #     i = 4
    #     print("pq.insert(", i, ")")
    #     pq.insert(i)
    #     self.assertEqual(pq.min(), 3)
    #     i = 2
    #     print("pq.insert(", i, ")")
    #     pq.insert(i)
    #     self.assertEqual(pq.min(), 2)
    #     self.assertEqual(pq.del_min(), 2)
    #
    # def test_pq4(self):
    #
    #     arr = [5, 2, 3, 4, 1]
    #     print(arr)
    #     pq = MinPQ(arr)
    #     print("pq.heapify(",arr,")")
    #     self.assertEqual(pq.size(), 5)
    #     self.assertEqual(pq.capacity, 5)
    #     self.assertFalse(pq.is_empty())
    #     self.assertEqual(pq.min(), 1)
    #     self.assertEqual(pq.del_min(), 1)
    #     self.assertEqual(pq.del_min(), 2)
    #     self.assertEqual(pq.del_min(), 3)
    #     self.assertEqual(pq.del_min(), 4)
    #     self.assertEqual(pq.del_min(), 5)
    #     self.assertTrue(pq.is_empty())

if __name__ == '__main__':
    unittest.main()
