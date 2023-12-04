def classify(number):
    if number <= 0:
        raise ValueError('Only numbers > 0')
    if not isinstance(number, int):
        raise ValueError(f'input{number} must be integer')
                
    n_list = 0
    for i in range(1, number + 1):
        if number % i == 0 and i != number:
            n_list += i
    
    if n_list == number:
        return "perfect"
    elif n_list > number:
        return "abundant"
    elif n_list < number:
        return "deficient"

