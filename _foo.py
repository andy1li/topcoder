# https://arena.topcoder.com/

import math

class AAA(object):
    def _mrange(self, start, stop, step):
        while start < stop:
            yield start
            start += step
    
    def _is_prime(self, a):
        if a < 2:
            return False
        elif a == 2:
            return True
        elif a % 2 == 0:
            return False
        return all(a % i for i in self._mrange(3, (math.sqrt(a))+2, 2))
       
    def bbb(self, n):
        result = n
        return 0
      

foo = AAA()
print foo.bbb(101)



'''


'''
