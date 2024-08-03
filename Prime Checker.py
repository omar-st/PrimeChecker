import time
from itertools import islice

def take(n, iterable):
    """Return the first n items of the iterable as a list."""
    return list(islice(iterable, n))

def get_primes(max):
    comp = {}
    prim = {}
    return seive(max, comp, prim)[0]

def seive(max, comp, prim):
    start = time.time()
    for i in range(2, max):
        if i in comp:
            continue
        else:
            prim[i] = True
            for j in range(i*2, max, i):
                comp[j] = True
    end = time.time()
    print(max, "numbers tested in", end - start, "sec")
    return (prim, comp)

#print(get_primes(max))

def is_prime(n, primes):
    if n in primes:
        return 1
    else: 
        return 0

def read(max, primes):
    #print(primes)
    print("This program checks if a number less than", max, "is prime.")
    while True:
        num = input('Number to check: ')
        if len(num) == 0:
            break
        else:
            num = int(num)
            if num in primes:
                print(num, "is prime!")
            else:
                print("num is not prime")



if __name__ == "__main__":
    max=10**6
    siv = get_primes(max)
    read(max, siv)
