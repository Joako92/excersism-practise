##An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

def is_armstrong_number(number):
    num_list = list(str(number)) ##Convert the string in a list of integers
    results = []
    for n in num_list:
        r = int(n) ** len(str(number))
        results.append(r)
        
    if number == sum(results):
        return True
    else:
        return False

