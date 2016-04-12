# https://arena.topcoder.com/#/u/practiceCode/16715/8886/9988/1/328498

import math

class ExploringNumbers(object):
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

    def _next_num(self, n):
        result = map(lambda s: int(s)**2, str(n))
        return sum(result)        
        
    def numberOfSteps(self, n):
        result = n
        for i in self._mrange(0, n, 1):
            if result == 1:
                return -1
            if self._is_prime(result):
                print result, "is prime"
                return i+1
            result = self._next_num(result)
            #print result
        else:
            return -1
      

foo = ExploringNumbers()
print foo.numberOfSteps(57)



'''
0)
5
Returns: 1
The input itself is a prime.

1)
57
Returns: 4
Vasa will write down 57, 74 (= 5^2 + 7^2), 65 (= 7^2 + 4^2), and 61 (= 6^2 + 5^2). Number 61 is a prime.

2)
1
Returns: -1
Vasa begins by writing down the number 1. As 1 is not a prime, he is not done yet. As he already wrote down 1 element of the sequence without finding a prime, he becomes bored and leaves.

3)
6498501
Returns: 2

4)
989113
Returns: 6

5)
12366
Returns: -1
For n=12366 there are no primes among the first 12366 elements of Vasa's sequence.
'''
