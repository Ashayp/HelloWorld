import unittest

class TestHelloWorld(unittest.TestCase):
    def testHelloWorld(self): 
        self.assertEqual(1,1,'one equals one')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()