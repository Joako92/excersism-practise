def equilateral(sides):
    ##Check sides
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0 or sum(sides)-max(sides) < max(sides):
            return False

    if sides[0] == sides[1] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    ##Check sides
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0 or sum(sides)-max(sides) < max(sides):
            return False

    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]:
        return True
    return False


def scalene(sides):
    ##Check sides
    if len(sides) != 3:
        return False
    for side in sides:
        if side <= 0 or sum(sides)-max(sides) < max(sides):
            return False

    if sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]:
        return True
    return False

