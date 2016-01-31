'''
Created on Jan 27, 2016

@author: Fereydoun
'''
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
        
class testbase(Base):
    '''
    This is the base test template. The user need to add or modify the test method per test case
    '''
    def __init__(self, argv):
        self.argv = argv
        '''
        Constructor
        '''
        super(testbase, self).__init__()
        
    def test(self):
        '''
        Test method to be modified by testers/developers
        '''
        print 'calling supper class Base test function ...' 
        super(testbase,self).test()
        print "This is the testbase ..."
    def superclass_Method(self,method):
        print "calling supper class method: %s " % method
#         super(testbase, self).method
        if method == 'test':
            print"Executing test() method"
            super(testbase, self).test()
a = {"key1":1,"key2":{"key3":1,"key4":{"key5":4}}}
b = {"key1":1,"key2":{"key3":1,"key4":{"key5":4}},"key6":{"key7":1,"key8":{"key9":4, "key10":{"key11":1,"key12":{"key13":4}}}}}

def find_depth(d, keys_depth, depth):
    for k in d.keys():
        keys_depth[k] = 1 + depth
    for k, v in d.iteritems():
        if type(v) is dict:
            depth +=1
            find_depth(v, keys_depth, depth)
    return keys_depth

def print_depth(data):
    if not type(data) is dict:
        print "This is a function to evaluate key's depth for dict type data only ..."
        return 
    print "-__-" * 10
    ddepth = check_depth(data)
    for k in sorted(ddepth):
        print k, ddepth[k]
    return ddepth
def check_depth(data, dp={}, depth=1):
    for k, v in data.iteritems():
        dp.setdefault(k, depth)
        if type(v) is dict:
            check_depth(v, dp, dp[k] + 1)
    return dp
    
    
        
tb = testbase('a')
if __name__ == '__main__':
#     tb.test()
#     tb.superclass_Method("test")
    print print_depth(a)
    

