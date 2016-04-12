# https://arena.topcoder.com/#/u/practiceCode/1413/2747/2973/1/1413

class Genetics(object):
    def _allel(self, g1, g2, dom):
        if g1 == g2:
            return g1
        elif dom == 'D':
            return g1.upper()
        elif dom == 'R':
            return g1.lower()
       
    def getOffspring(self, g1, g2, dom):
        print g1, g2, dom
        result = map(self._allel, g1, g2, dom)
        return ''.join(result)
      

foo = Genetics()
print foo.getOffspring("ABCDEFG", "abcdefg", "DDRRRDR")



'''
0)
"AAAA"
"AAaa"
"DRDR"
Returns: "AAAa"
Whenever there are two 'A's, the return character is an 'A', and when there is one 'A' and one 'a', the return character is an 'A' only if the corresponding character in dom is a 'D'.

1)
"ABCDEFG"
"abcdefg"
"DDRRRDR"
Returns: "ABcdeFg"

2)
"Z"
"z"
"D"
Returns: "Z"

3)
"MGskgzTFQoclnDjZu"
"mgSKGzTFQoClnDJzU"
"DDDDDRDDDDRDDDDDD"
Returns: "MGSKGzTFQoclnDJZU"

'''
