'''
Write a generator that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

A candidate number x is prime if (x % p) != 0 for all earlier primes p.
'''

def genPrimes():
    primes = []
    last = 1
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last

p = genPrimes()

p.next()
