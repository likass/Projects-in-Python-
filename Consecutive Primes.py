def return_primes(upto=100):
    primes = []
    sieve = set()
    for i in xrange(2, upto+1):
        if i not in sieve:
            primes.append(i)
            sieve.update(range(i, upto+1, i))
    return primes

def find_prime_sum_of_most_consecutive_primes_under(x):
    '''
    given x, an integer, return the prime that is the sum
    of the greatest number of consecutive primes under x
    '''
    primes = return_primes(x)
    length = len(primes)
    primeset = set(primes)
    maxprime = primes[-1] # last prime
    result = None
    min_length = 1
    for start in xrange(0, length):
        for window_length in xrange(start + min_length, length - start + 1):
            check_primes = primes[start:window_length]
            s = sum(check_primes)
            if s in primeset:
                min_length = len(check_primes)
                result = s
            elif s > maxprime:
                break
    return result
