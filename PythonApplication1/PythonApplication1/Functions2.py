import doctest
import math

def is_prime(number):
    if number < 2:
        return False
    for x in range(2, int(math.sqrt(number) + 1)):
        if number % x == 0:
            return False
    else:
        return True


#def primes(n): # simple Sieve of Eratosthenes
#   odds = range(3, n+1, 2)
#   sieve = set(sum([range(q*q, n+1, q+q) for q in odds],[]))
#   return [2] + [p for p in odds if p not in sieve]


def primes_max(n):
    yield 2
    for number in range(3, n, 2):
        if is_prime(number):
            yield number

def emulate_map(func, iterable):
    return iter([func(i) for i in iterable])

print(is_prime(37))
print(is_prime(777))
#print(list(primes_max(200)))
print(list(emulate_map(int, iter(['1', '5', '8']))))

print 


