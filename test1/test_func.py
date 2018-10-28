# test_func.py

import unittest # std lib 
import func     # import module being tested

class TestFunc(unittest.TestCase):

## failing testcase    
#    def test_fail(self):
#        self.assertEqual(1,0)
        
    def test_add(self):
        sum = func.add(1, 2)
        self.assertEqual(sum, 3)

        sum = func.add(100, 0)
        self.assertEqual(sum, 100)

    def test_sub(self):
        diff = func.sub(10, 2)
        self.assertEqual(diff, 8)


if __name__ == '__main__':
    unittest.main()
