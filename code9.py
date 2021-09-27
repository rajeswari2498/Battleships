def getPopulation(cities):
    total=0
    for i in range(len(cities)):
        total = total + cities[i][2]
    return total
cities = [ ["Pittsburgh", "Allegheny", 302407],
               ["Philadelphia", "Philadelphia", 1584981],
               ["Allentown", "Lehigh", 123838],
               ["Erie", "Erie", 97639],
               ["Scranton", "Lackawanna", 77182] ]
print(getPopulation(cities))
