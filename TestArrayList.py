import unittest
from ArrayList import ArrayList, EmptyError

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
        self.assertTrue(al.get(2) == 7 and al.get(4)==16)

    def test_add_at_end(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        al.add(7,3)
        self.assertTrue(al.get(3) == 7 and al.get(4)==16)

    def test_add_at_start(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        al.add(7,0)
        self.assertTrue(al.get(0) == 7 and al.get(1)==1)

    def test_add_index_full_array(self):
        data = [1,4,6,16]
        al = ArrayList(capacity=4)
        for e in data:
            al.add(e)
        al.add(7,0)
        self.assertTrue(al.get(0) == 7 and al.get(1)==1)

    def test_clear_array_list(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
    
        al.clear()

        self.assertTrue(al.isEmpty(), al.size == 0)


    def test_set_at_index(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        previous_element = al.set(2,10)
        self.assertTrue(al.get(2)==10, previous_element == 10)

    def test_set_at_index_out_of_range(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        with self.assertRaises(IndexError):
            previous_element = al.set(100000,1)

    def test_remove_element(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        element = al.remove()
        self.assertTrue(al.size() == 3 and element == 16)

    def test_remove_element_from_empty(self):
        al = ArrayList()
        with self.assertRaises(EmptyError):
            element = al.remove()

    def test_remove_element_at_index(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        element = al.remove(1)
        self.assertTrue(al.size() == 3 and element == 4 and al.get(0) == 1 and al.get(1) == 6)

    def test_remove_element_at_index_start(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        element = al.remove(0)
        self.assertTrue(al.size() == 3 and element == 1 and al.get(0) == 4 and al.get(2) == 16)

    def test_remove_element_at_index_end(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        element = al.remove(3)
        self.assertTrue(al.size() == 3 and element == 16 and al.get(0) == 1 and al.get(2) == 6)

    def test_to_string(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        self.assertTrue(str(data) == str(al))

    def test_eq_py_list(self):
        data = [1,4,6,16]
        al = ArrayList()
        for e in data:
            al.add(e)
        self.assertTrue(al == data)

    def test_eq(self):
        data = [1,4,6,16]
        al = ArrayList()
        al2 = ArrayList()
        for e in data:
            al.add(e)
            al2.add(e)
        self.assertTrue(al == al2)



if __name__ == '__main__':
    unittest.main()