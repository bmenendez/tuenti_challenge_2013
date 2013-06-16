#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys, os

PREVIOUS = 5

def usage(message):
    print '------------------------------------------------------------------'
    print 'There was an error during the interpretation of the pararmeters: '
    print message
    print 'Please, enter it correctly'
    print '------------------------------------------------------------------'
    
class MySuggestions():
    def __init__(self, dictFile):
        self.name = dictFile
        self.dict = []
        self.sugs = []
        
    def loadDictionary(self):
        f = open(self.name, 'r')
        allLines = f.readlines()
        f.close()
        for line in allLines:
            self.dict.append(line.split('\n')[0])
        
    def getSuggestions(self):
        self.sugs.sort()
        return self.sugs
        
    def analyze(self, word):
        self.sugs = []
        letters = {}
        for w in self.dict:
            cont = True
            for l in word:
                if not l in letters:
                    occurrencesW = w.count(l)
                    if occurrencesW == 0:
                        cont = False
                        break
                    occurrencesL = word.count(l)
                    if occurrencesL != occurrencesW:
                        cont = False
                        break
                    letters[l] = occurrencesL
            if cont:
                for l in w:
                    if not l in letters:
                        cont = False
                        break
                if cont and (w != word):
                    self.sugs.append(w)
                    
            letters.clear()
            
        return 0
    
if __name__ == '__main__':
    dictFile = ''
    number = -1
    i = 0
    while i != PREVIOUS:
        line = sys.stdin.readline().split('\n')[0]
        try:
            line = line.split()[0]
        except IndexError:
            usage('A blank line is not valid')
            sys.exit()
        
        if i % 2 == 0:
            if not line.startswith('#'):
                usage('There is a comment line without comments')
                sys.exit()
                
        else:
            if i == 1:
                dictFile = os.path.join(os.getcwd(), line)
                if not os.path.exists(dictFile):
                    usage('The file specified does not exist')
                    sys.exit()
                if not os.path.isfile(dictFile):
                    usage('The file specified is not a file')
                    sys.exit()
                
            elif i == 3:
                try:
                    number = int(line)
                    if number < 1:
                        usage('Number of words provided must be a positive number (>0)')
                        sys.exit()
                except ValueError:
                    usage('Number of words provided must be a number')
                    sys.exit()
            
        i += 1
        
    sugs = MySuggestions(dictFile)
    sugs.loadDictionary()
    
    i = 0
    for line in sys.stdin:
        try:                
            word = line.split()[0]
            if sugs.analyze(word) == 0:
                i += 1
                print word + ' -> ' + ' '.join(sugs.getSuggestions())
                
            if i == number:
                sys.exit()
        except IndexError:
            pass
