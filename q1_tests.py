import unittest
from q1 import custom_sort


class TestCustomSort(unittest.TestCase):
    
    def test_ordinary_sort(self):
        self.assertEqual(custom_sort([4,2,3,1]), [1,2,3,4])
        
    def test_frequency_sort(self):
        self.assertEqual(custom_sort([1,1,1,1,2,2,2,3,3,4]), [4,3,3,2,2,2,1,1,1,1])
        
    def test_mixed_frequency_and_ordinary(self):
        self.assertEqual(custom_sort([4,5,6,5,4,3]), [3,6,4,4,5,5])
        self.assertEqual(custom_sort([100,1,5,100,5,1000]), [1,1000,5,5,100,100])
        
    def test_negative_numbers(self):
        self.assertEqual(custom_sort([-9,1,1,2,3,-9]), [2,3,-9,-9,1,1])
        

if __name__ == '__main__':
    unittest.main()
    