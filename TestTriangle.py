# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    
    # Using the same test methodology I used in the previous assignment,
    # kept it simple to follow existing format.
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4,5,7),'Scalene','4,5,7 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(4,7,5),'Scalene','4,7,5 is a Scalene triangle')

    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(3,3,5),'Isosceles','3,3,5 is an Isosceles triangle')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(3,5,3),'Isosceles','3,5,3 is an Isosceles triangle')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(2,4,8),'NotATriangle','2,4,8 is not a triangle')

    def testInvalidInput(self):
        self.assertEqual(classifyTriangle(1,0,-2),'InvalidInput','1,0,-2 is an Invalid Input')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

