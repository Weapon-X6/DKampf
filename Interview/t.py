# for x in range(2, 101):
#     for y in range(2, x):
#         if x % y == 0:
#             break
#     else:
#         print(x, end=" ")

# for x in range(2, 101):
#     [x % y == 0 ? break: print(x, end=" ") for y in range(2, x)]
# primes = [x for x in range(2, 101) if all(x % y != 0 for y in range(2, x))]
# print(primes)

primes = (x for x in range(2, 101) if all(x % y != 0 for y in range(2, x)))
print(primes)
print(type(primes))
# primes = ([x for x in range(2, 101) if all(x % y != 0 for y in range(2, x))])
# print(list(primes))
