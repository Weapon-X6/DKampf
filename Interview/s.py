def prime_generator():
    for x in range(2, 101):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            yield x


for n in prime_generator():
    print(n, end=" ")
    print("times 2 = ", n*2)


primes = prime_generator()
print(next(primes))
print(next(primes))
print(next(primes))
wsta
