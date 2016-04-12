# https://arena.topcoder.com/#/u/practiceCode/16705/48887/13934/1/328359

class EllysTimeMachine (object):
    def hToM(self, h):
        m = int(h)*5
        if m == 60:
            m = 0
        return '{:02d}'.format(m)
        
    def mToH(self, m):
        h = int(m)/5
        if h == 0:
            h = 12
        return '{:02d}'.format(h)
        
    def getTime(self, time):
        (h, m) = time.split(':')
        #print h, m, self.mToH(m), self.hToM(h)
        
        return self.mToH(m)+':'+self.hToM(h)
      

foo = EllysTimeMachine()
print foo.getTime("01:00")


'''
0)
"11:20"
Returns: "04:55"
The example from the problem statement.

1)
"02:25"
Returns: "05:10"

2)
"06:30"
Returns: "06:30"

3)
"05:55"
Returns: "11:25"

4)
"03:45"
Returns: "09:15"

5)
"01:00"
Returns: "12:05"
'''
