import unittest
from ArrayList import ArrayList

class TestArrayListMethods(unittest.TestCase):

    def test_isEmpty(self):
        al = ArrayList()
        self.assertTrue(al.isEmpty() and al.size()==0)

    def test_get_empty_array(self):
        al = ArrayList()
        with self.assertRaises(IndexError):
            al.get(0)
    
    def test_get_empty_array(self):
        al = ArrayList()
        al.add(4)
        self.assertEqual(4,al.get(0))
            


    def test_add_one_element(self):
        al = ArrayList()
        al.add(1)
        self.assertTrue(al.size() == 1)

    def test_add_full_array(self):
        data = [1,4,6,16,0,33,111,2,6,11]
        al = ArrayList()
        for e in data:
            al.add(e)
        al.add(2)
        self.assertTrue(al.get(10) == 2)

    def test_add_at_index(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        al.add(7,2)
        self.assertTrue(al.get(2) == 7)






if __name__ == '__main__':
    unittest.main()