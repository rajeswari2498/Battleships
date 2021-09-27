def getCounty(cities, cityName):
    for i in range(len(cities)):
        entry = cities[i] # entry is a list
        if entry[1] == cityName:
            return entry[1]
    return None # city not found
cities = [ ["Pittsburgh", "Allegheny", 302407],
               ["Philadelphia", "Philadelphia", 1584981],
               ["Allentown", "Lehigh", 123838],
               ["Erie", "Erie", 97639],
               ["Scranton", "Lackawanna", 77182] ]
print(getCounty(cities,"Lehigh"))


def getFactors(n):
    factors = [ ]
    for num in range(1, n+1):# num is a possible factor
        if n % num == 0:
            factors.append(num)
    return factors
print(getFactors(20))


lst = [ 1, 2, "a" ]
lst.insert(1, "foo")
lst.remove("a")
lst.pop(0)
print(lst)