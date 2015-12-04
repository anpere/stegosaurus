
## O(p)
def generatorLength(g,p):
    values={}
    length = 0
    value = 1
    for i in xrange(p):
        value = (value*g)%p
        if values.get(value,0) == 1:
            break
        else:
            values[value]=1
            length+=1
    return length

def isPrime(p):
    isPrime = True
    for i in range(p):
         isPrime &= p%i!=0
## O(p^2)
def findGenerator(p):
    for g in xrange(p):
        if generatorLength(g,p) == p-1:
            print g

if __name__ == "__main__":
    findGenerator(262147)
