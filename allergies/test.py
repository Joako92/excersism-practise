
items = {"eggs":1,"peanuts":2,"shellfish":4,"strawberries":8,"tomatoes":16,"chocolate":32,"pollen":64,"cats":128,}
allergies = []
item = 18

for i in reversed(sorted(items.values())):
    if item - i >= 0:           
        allergies.append(list(items.keys())[list(items.values()).index(i)])
        item -= i

print(allergies)
