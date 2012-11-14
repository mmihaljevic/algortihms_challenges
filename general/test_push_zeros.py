# test case for push_zeros

import unittest
import push_zeros as p

class TestPushZeros(unittest.TestCase):
    
    def set_up(self):
        pass

    def test_wrong_input(self):
        array = None
        self.assertEqual(False, p.push_zeros(array))

    def test_all_zerros(self):
        array = [0,0,0,0,0,0,0]
        self.assertEqual(array, p.push_zeros(array))

    def test_none_zeros(self):
        array = [1,2,5,6,7,8,11]
        self.assertEqual(array, p.push_zeros(array))

    def test_average_zeros(self):
        array = [1,2,0,4,0,0,8]
        self.assertEqual([1,2,4,8,0,0,0], p.push_zeros(array))

    def tear_down(self):
        pass

if __name__ == '__main__':
    unittest.main()

