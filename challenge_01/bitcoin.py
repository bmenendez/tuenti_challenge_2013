#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys

def usage(message):
    print '------------------------------------------------------------------'
    print 'There was an error during the interpretation of the pararmeters: '
    print message
    print 'Please, enter it correctly'
    print '------------------------------------------------------------------'
    
class MyBitcoin():
    def __init__(self, euros):
        self.euros = euros
        self.bitcoins = 0
        self.state = 'neutral' # possible states: neutral, pos, neg
        self.messageError = 'Impossible to obtain: there is a non-integer value in this exchange rate'
        
    def doTheChanges(self, previous, current):
        if (current > previous) and ((self.state == 'neutral') or (self.state == 'neg')) and (self.euros >= previous):
            self.bitcoins = self.euros / previous
            self.state = 'pos'
        elif (current < previous) and (self.state == 'neutral'):
            self.state = 'neg'
        elif (current < previous) and (self.state == 'pos') and (self.bitcoins != 0):
            self.euros = self.bitcoins * previous
            self.state = 'neg'
            
    def getEuros(self):
        return self.euros
        
    def analyze(self, fluctuation):
        firstValue = 0
        previousValue = 0
        try:
            firstValue = int(fluctuation[0])
            previousValue = int(fluctuation.pop(0))
        except ValueError:
            usage(self.messageError)
            return -1
        except IndexError:
            usage('There are no numbers in this exchange rate')
            return -1
            
        for i in range(len(fluctuation)):
            currentValue = 0
            try:
                currentValue = int(fluctuation[i])
            except ValueError:
                usage(self.messageError)
                return -1
                
            if currentValue <= 0:
                usage('Impossible to obtain: there is a zero or negative value in this exchange rate')
                return -1
            
            self.doTheChanges(previousValue, currentValue)
                
            previousValue = currentValue
            
        if len(fluctuation) == 0:
            pass
        elif (len(fluctuation) == 1) and (currentValue > firstValue) and (self.bitcoins != 0):
            self.euros = self.bitcoins * currentValue
        elif (len(fluctuation) == 1):
            pass
        elif (int(fluctuation[-1]) > int(fluctuation[-2])) and (self.bitcoins != 0):
            self.euros = self.bitcoins * (int(fluctuation[-1]))
            
        return 0

if __name__ == '__main__':
    i = -1
    number = 0
    bitcoin = ''
    cont = True
    for line in sys.stdin:
        if i == -1:
            number = 0
            try:
                number = 2*int(line.split()[0])
                i = 0
                if number <= 0:
                    usage('First parameter must be greater than zero')
                    sys.exit()
            except ValueError:
                usage('First parameter was not a number')
                sys.exit()
            
        else:
            if i % 2 == 0:
                euros = 0
                
                try:
                    euros = int(line.split()[0])
                except ValueError:
                    usage('This value "' + line.split()[0] + '" is not a number for euros')
                    cont = False
                    
                if (euros <= 0) or (euros > 100):
                    if cont:
                        usage('Number of euros must be greater than zero and less than 101')
                        cont = False
                else:
                    bitcoin = MyBitcoin(euros)
                    cont = True
            else:
                if cont:
                    if bitcoin.analyze(line.split()) == 0:
                        print bitcoin.getEuros()
                
            i += 1

            if i == number:
                # Bye! Thank you for coming!
                sys.exit()
