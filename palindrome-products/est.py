factors = tuple(n for n in range(1,3))

new_dict = dict.fromkeys(factors,[])
print(new_dict)

for num in factors:
        for num2 in factors:
            product = num2 * num
            print(list(new_dict.keys()))
            if product in list(new_dict.keys()):
                print(product)
                print(new_dict[product])
                new_dict[product].append([num,num2])
                print(new_dict)
##            new_dict.update({product:[num,num2]})

print(new_dict)
