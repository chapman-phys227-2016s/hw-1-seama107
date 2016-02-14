#!/usr/bin/python

def find_primes(n):
    """
    Finds all the primes below number n using the sieve of Eratosthenes
    """
    candidates = [i + 2 for i in range(n-1)]
    for p in candidates:
        for i in candidates:
            if i % p == 0 and p != i:
                candidates.remove(i)
    return candidates

def test_primes(n = 100):
    """
    Tests each integer lower than the square root of number n in the list
    of primes to see if it's divisible by it
    """
    list_primes = find_primes(n)
    for n in list_primes:
        for i in range(int(n ** .5))[2:]:
            assert(n % i != 0)
    