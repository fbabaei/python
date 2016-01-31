'''
Created on Jan 27, 2016

@author: Fereydoun
'''
import time
import logging
import sys, os, threading

class Base(object):
    '''
    This is the base class for the platform project
    '''
    def __init__(self):
        '''
        Constructor
        '''
    def Environment(self):
        '''
        Base required environment setup 
        '''   
    def Storage(self):
        '''
        Backup target
        '''
    def test(self):
        '''
        This is the test function to be modified by the test class
        '''
        print "The Base test method ..."
class testbase(object):
    '''
    This is the base test template. The user need to add or modify the test method per test case
    '''
    def __init__(self, argv):
        self.argv = argv
        '''
        Constructor
        '''
        self.Base = Base()
        
    def test(self):
        '''
        Test method to be modified by testers/developers
        '''
        print 'calling supper class Base test function ...' 
        self.Base.test()
        print "This is the testbase ..."
    def Base_Method(self,method):
        print "calling supper class method: %s " % method
#         super(testbase, self).method
        if method == 'test':
            print"Executing test() method"
            self.Base.test()

tb = testbase('a')
if __name__ == '__main__':
#     tb.test()
    tb.Base_Method("test")
    