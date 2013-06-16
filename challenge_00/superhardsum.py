#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    for line in sys.stdin:
        total = 0
        lSplitted = line.split()
        for ls in lSplitted:
            try:
                total += int(ls)
            except:
                pass
                
        print str(total)
