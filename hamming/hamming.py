def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("strands must be exact length.")
    else:
        distance = 0
        counter = 0
        for n in list(strand_a):
            if n == list(strand_b)[counter]:
                counter += 1      
            else:
                distance += 1
                counter += 1
       
        return distance

##BOBAHOP'S
        
def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Lengths must be the same")
    return sum(char_a != char_b for char_a, char_b in zip(strand_a, strand_b))
