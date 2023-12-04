def factors(value):
    factors = []
    while value != 1:
        for i in range(2, value +1):
            if (value % i) == 0:              
                value = int(value / i)
                factors.append(i)
                break
    return factors


