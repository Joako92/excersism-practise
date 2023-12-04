def sum_of_multiples(limit, multiples):
    result = []
    for multiple in multiples:
        result.extend( [multiple*num for num in range(limit) if multiple*num < limit if multiple*num not in result] )
    return sum(result)

