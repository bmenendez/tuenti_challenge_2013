#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

symbols = ['<', '>', '.']

def usage(message):
    print '------------------------------------------------------------------'
    print 'There was an error during the interpretation of the pararmeters: '
    print message
    print 'Please, enter it correctly'
    print '------------------------------------------------------------------'
    
class MyScripts():
    def __init__(self):
        self.op = []
        self.text = []
        self.response = ''
        
    def getResponse(self):
        return self.response
        
    def divide(self, eText):
        myS = ''
        for l in eText:
            if l in symbols:
                self.text.append(myS)
                myS = ''
                self.op.append(l)
            else:
                myS += l
        self.text.append(myS.split('\n')[0])
        self.text.pop(0)
        
    def whatWouldItBe(self):
        self.response = ''
        correct = True
        ended = False
        totalLess = 0
        totalMore = 0
        i = -1
        
        while not ended:
            i += 1
            if i >= len(self.op) - 1:
                break
            text = self.text[i]
            try:
                idx2 = self.text[i+1:].index(text)
                sym = self.op[i+1:][idx2]
                if self.op[i] == '.':
                    if sym != '<':
                        return -1
                    self.op.pop(i + idx2 + 1)
                    self.text.pop(i + idx2 + 1)
                elif self.op[i] == '>':
                    if sym != '<':
                        self.op.pop(i)
                        self.text.pop(i)
                        if i != 0:
                            i -= 1
                    else:
                        if idx2 == 0:
                            return -1
                        self.op[i] = '.'
                        self.op.pop(i + idx2 + 1)
                        self.text.pop(i + idx2 + 1)
                        if idx2 > 1:
                            correct = False
                elif self.op[i] == '<':
                    if sym != '<':
                        return -1
                    self.op.pop(i)
                    self.text.pop(i)
                    if i != 0:
                        i -= 1
            except ValueError:
                if self.op[i] == '>':
                    if i < len(self.op) - 1:
                        totalMore += 1
                        if totalMore > 1:
                            return -1
                    else:
                        self.op[i] = '.'
                elif self.op[i] == '<':
                    if i > 1:
                        totalLess += 1
                        if totalLess > 1:
                            return -1
                    elif i == 1:
                        self.text[1] = self.text[0]
                        self.text[0] = text
                        self.op[1] = '.'
                    else:
                        return -1
                        
        if (totalMore == 1) or (totalLess == 1):
            correct = False
            
        if correct:
            return 0
        else:
            return 1
        
    def analyze(self, entireText):
        self.op = []
        self.text = []
        self.divide(entireText)
        
        response = self.whatWouldItBe()
        if response == -1:
            self.response = 'invalid'
        elif response == 0:
            self.response = ','.join(self.text)
        else:
            self.response = 'valid'

if __name__ == '__main__':
    line = sys.stdin.readline().split('\n')[0]
    number = 0
    try:
        number = int(line.split()[0])
        if number < 1:
            usage('A positive number must be given')
            sys.exit()
    except IndexError:
        usage('A blank line is not valid')
        sys.exit()
    except ValueError:
        usage('An integer must be given')
        sys.exit()
    
    scrs = MyScripts()    
    i = 0
    for script in sys.stdin:
        scrs.analyze(script)
        print scrs.getResponse()
        i += 1
        if i == number:
            break
    
    sys.exit()
