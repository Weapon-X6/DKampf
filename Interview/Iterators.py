from turtle import fd


cities = ['Alberta', 'Berlin', 'Brno']

for city in cities:
    print(city)


# with iterators
iter_cities = iter(cities)

while True:
    try:
        city = next(iter_cities)
        print(city)
    except StopIteration:
        break
