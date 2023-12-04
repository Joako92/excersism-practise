def is_valid(isbn):
    clean = [n for n in isbn if n.isnumeric() or n == "X"]
    if len(clean) != 10 or "X" in clean[0:9]:
        return False
    if clean[9] == "X":
        clean[9] = 10
    if sum(int(a) * b for a,b in zip(clean,list(range(10,0,-1)))) % 11 == 0:
        return True
    return False


