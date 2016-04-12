# https://arena.topcoder.com/#/u/practiceCode/1282/1262/1333/2/1282

class Substitute(object):
    def _substitute(self, c):
        d = self.key.find(c)+1
        print c, self.key, d
        if d < 1:
            d = '-'
        if d == len(self.key):
            d = 0
            
        return str(d)
        
    def getValue(self, key, code):
        self.key = key
        result = map(self._substitute, code)
        result = filter(lambda x: x != '-', result)
        
        return int(''.join(result))

foo = Substitute()
print foo.getValue("TRADINGFEW", "LGXWEV")

'''
Examples
0)
"TRADINGFEW"
"LGXWEV"
Returns: 709
The L,X, and V are ignored since they do not appear in the key. 
G is the seventh letter in the key, W is the 10th letter, and E is the 9th letter.

1)
"ABCDEFGHIJ"
"XJ"
Returns: 0

2)
"CRYSTALBUM"
"MMA"
Returns: 6
'''