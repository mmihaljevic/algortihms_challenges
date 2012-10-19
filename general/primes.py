# find first 100 prime numbers

def primes():
    primes = [2]
    first = 3
    while len(primes) != 100:
        is_prime = True
        for i in primes:
            if first % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(first)
        first +=1
        
    return primes

print primes()
