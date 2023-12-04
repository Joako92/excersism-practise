def largest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError ("min is biger then max")
    factors = []
    value = None    
    max_product = min_factor**2
    
    for num in range(max_factor,min_factor -1,-1):
        for num2 in range(num,min_factor - 1,-1):
            if str(num * num2) == str(num * num2)[::-1]:
                if num*num2 > max_product:
                    max_product = num*num2
                    value = max_product
                    factors = [sorted([num,num2])]
                    break
                elif num*num2 == max_product:
                    factors.append([num,num2])
                    break
                
    return value, factors


def smallest(min_factor, max_factor):
    if min_factor > max_factor:
        raise ValueError ("factors in wrong order.")
    factors = []
    value = None
    min_product = max_factor**2

    for num in range(min_factor,max_factor + 1):
        for num2 in range(num,max_factor + 1):
            if str(num * num2) == str(num * num2)[::-1]:
                if num*num2 < min_product:
                    min_product = num*num2
                    value = min_product
                    factors = [sorted([num,num2])]
                    break
                elif num*num2 == min_product:
                    factors.append([num,num2])
                    break
          
    return value, factors

