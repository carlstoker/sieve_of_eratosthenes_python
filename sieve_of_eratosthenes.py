#!/usr/bin/env python3
"""Sieve of Eratosthenes
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""
from sys import argv


def prime_sieve(n):
    sieve = [True] * n
    sieve[0:2] = [False] * 2

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            pointer = i ** 2
            while pointer < n:
                sieve[pointer] = False
                pointer += i

    return [i for i in range(len(sieve)) if sieve[i]]


for arg in argv[1:]:
    primes = prime_sieve(int(arg))
    print('{0:,} primes found through {1:,}: {2}'.format(len(primes), int(arg), primes))
