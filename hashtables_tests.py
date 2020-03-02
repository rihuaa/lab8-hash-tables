import unittest

from hashtables import HashTableSepchain #, HashTableLinear, HashTableQuadratic
from hashtables import hash_string, import_stopwords, enlarge

class MyTest(unittest.TestCase):
    # hash of 'us', 'say' is 2
    def test_HashTableSepChain(self):
        t = HashTableSepchain()

        self.assertEqual(t.size(), 0)
        self.assertFalse(t.contains('us'))
        self.assertRaises(KeyError, t.get, 'us')

        t.put('us', 'us')
        self.assertEqual(t.get('us'), 'us')
        self.assertEqual(t['us'], 'us')
        self.assertTrue(t.contains('us'))
        self.assertFalse(t.contains('say'))
        self.assertEqual(t.size(), 1)
        self.assertEqual(t.collisions(), 0)

        t.put('say', 'say')
        self.assertEqual(t.get('say'), 'say')
        self.assertTrue(t.contains('say'))
        self.assertEqual(t.size(), 2)
        self.assertEqual(t.collisions(), 1)

        t.remove('say')
        self.assertFalse(t.contains('say'))
        self.assertTrue(t.contains('us'))
        t.remove('us')
        self.assertEqual(t.size(), 0)

        print(hash_string('the', 11)) # 'the' = 5
        t.put('us', 'us')
        t.put('say', 'say')
        t.put('the', 'the')
        self.assertTrue(t.contains('the'))
        self.assertEqual(t.load_factor(), 0.2727272727272727)


        # print(t)
        # print(t['say'])
        # stop = 'stop_words.txt'
        # with open(stop) as data:
        #     for line in data:
        #         for word in line.split():
        #             hashed = hash_string(word, 11)
        #             if hashed == 2:
        #                 print(word)

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
