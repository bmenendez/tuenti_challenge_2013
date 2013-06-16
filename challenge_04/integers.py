#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, struct
from bitstring import BitArray

def usage(message):
    print '------------------------------------------------------------------'
    print 'There was an error during the interpretation of the pararmeters: '
    print message
    print 'Please, enter it correctly'
    print '------------------------------------------------------------------'
    
class MyIntegers():
    def __init__(self, lst):
        self.lst = lst
        self.missing = []
        
    def printSolution(self):
        for idx in self.lst:
            print str(self.missing[idx])
            
    def analyze(self):
        numbers = BitArray(2**32)
        numbers.set(False, xrange(0, 2**32))
        
        f = open('integers', 'rb')
        for line in f:
            data = ''
            if len(line) < 2:
                data, = struct.unpack('B', line[:1])
            elif len(line) < 4:
                data, = struct.unpack('H', line[:2])
            else:
                data, = struct.unpack('I', line[:4])
            
            numbers[data] = True
        f.close()
        
        self.missing = []
        for i in xrange(2**32):
            if not numbers[i]:
                self.missing.append(numbers[i])

if __name__ == '__main__':
    line = sys.stdin.readline().split('\n')[0]
    num = 0
    try:
        num = int(line.split()[0])
        if num < 1:
            usage('A positive number must be given')
            sys.exit()
    except IndexError:
        usage('A blank line is not valid')
        sys.exit()
    except ValueError:
        usage('An integer must be given')
        sys.exit()
        
    i = 0
    analyzing = []
    for line in sys.stdin:
        try:
            n = int(line.split()[0])
            if (n < 1) or (n > 100):
                usage('A number between 1 and 100 (included) must be given')
            else:
                analyzing.append(n)
                i += 1
                if i == num:
                    break
        except IndexError:
            pass
        except ValueError:
            usage('An integer must be given')
    
    mintegers = MyIntegers(analyzing)
    mintegers.analyze()
    mintegers.printSolution()
    
    sys.exit()
