def steps(number):
    steps_cant = 0
    orbita_n = []
    if number < 1:
        raise ValueError("Only positive integers.")
    while number != 1:
        
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
        steps_cant += 1
        print("Paso", steps_cant, ":", number)
    return orbita_n


print("Orbita de N:", steps(10))
