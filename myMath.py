
## O(p)
def generatorLength(g,p):
    values={}
    length = 0
    for i in xrange(p):
        value = (g**i)%p
        if values.get(value,0) == 1:
            break
        else:
            values[value]=1
            length+=1
    return length
#    while(((g**i)%p) not in values):
#        values[(g**i)%p] = 0
#        values.append((g**i)%p)
#        i+=1

def isPrime(p):
    isPrime = True
    for i in range(p):
         isPrime &= p%i!=0
## O(p^2)
def findGenerator(p):
    for g in xrange(p):
        if generatorLength(g,p) == p-1:
            print g
