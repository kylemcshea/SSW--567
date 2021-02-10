'''
Created on Feb 8, 2015

@author: Kyle McShea

SSW 567 - Hw 01 Test Script
'''
import unittest
import triangle

class Test(unittest.TestCase):

    def test01(self):
        self.assertEqual(triangle.classify_triangle(10,10,10),"equilateral")
        self.assertEqual(triangle.classify_triangle(10,5,3),"scalene")
        self.assertEqual(triangle.classify_triangle(100,8,3),"scalene")
        self.assertEqual(triangle.classify_triangle(10,3,3),"isosceles")
        self.assertEqual(triangle.classify_triangle(10,10,3),"isosceles")
        self.assertEqual(triangle.classify_triangle(3,4,5),"right")
        self.assertEqual(triangle.classify_triangle(3,3,3),"equilateral")
        self.assertEqual(triangle.classify_triangle(24,10,26),"right")
        
if __name__ == "__main__":
    unittest.main()
