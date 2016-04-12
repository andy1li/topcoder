# https://arena.topcoder.com/#/u/practiceCode/1435/2824/3054/1/1435

import pprint

class Hex(object):
    def _marks_to_dict(self, marks):
        result = {}
        for mark in marks:
            result[mark[:2]] = mark[-1]
        return result

    def picture(self, n, marks):
        result = []
        self.marks = self._marks_to_dict(marks)
        
        # change '' to ' ' if printing is needed
        self.result = [['' for i in range(2*n+1)] for j in range(3*n)]
        # print n, self.marks
        # pprint.pprint(self.result)
        
        for i in range(0, 2*n, 2):
            for j in range(0, 2*n, 2):
                y = i + j/2
                x = j
                
                self.result[y][x+1] = '_'
                self.result[y+1][x] = '/'
                self.result[y+1][x+2] = '\\'
                self.result[y+2][x] = '\\'
                self.result[y+2][x+1] = '_'
                self.result[y+2][x+2] = '/'

                # print str(j/2), str(i/2)
                if self.marks.get(str(j/2)+str(i/2)):
                    self.result[y+1][x+1] = self.marks[str(j/2)+str(i/2)]
                else:
                    self.result[y+1][x+1] = ' '

        # pprint.pprint(self.result)     
        return map(lambda x: ''.join(x), self.result)
      
        

foo = Hex()
for line in foo.picture(4, ["00h","21h","01v","03v","02v"]):
    print line


'''
Examples
0)
4
{"00h","21h","01v","03v","02v"}
Returns: { " _", "/h\\_", "\\_/ \\_", "/v\\_/ \\_", "\\_/ \\_/ \\", "/v\\_/h\\_/", "\\_/ \\_/ \\", "/v\\_/ \\_/", "\\_/ \\_/ \\", " \\_/ \\_/", " \\_/ \\", " \\_/" }
Note that the elements in the returns are shown as string literals, so each backslash character in each is shown as \\. 
So, for example, the second element of this return should contain just 4 characters (i.e. its length would be 4). 
This will print the following 4x4 picture:
 _
/h\_
\_/ \_
/v\_/ \_
\_/ \_/ \
/v\_/h\_/
\_/ \_/ \
/v\_/ \_/
\_/ \_/ \
  \_/ \_/
    \_/ \
      \_/

1)
3
{"00v","01v","02v","11h","21h"}
Returns: { " _", "/v\\_", "\\_/ \\_", "/v\\_/ \\", "\\_/h\\_/", "/v\\_/h\\", "\\_/ \\_/", " \\_/ \\", " \\_/" }
This will print the following 3x3 picture:
 _
/v\_
\_/ \_
/v\_/ \
\_/h\_/
/v\_/h\
\_/ \_/
  \_/ \
    \_/

'''
