import unittest
from app import add
class TestApp(inittest.TestCase):
    def Test_add(self):
        self.asserEqual(add(2,3),5)
        self.asserEqual(add(10,3),13)
        self.asserEqual(add(1,3),4)
        self.asserEqual(add(11,12),23)
if __name__=='__main__':
    unittest.main()
