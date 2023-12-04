def is_valid(isbn):
    clean = [n for n in isbn if n.isnumeric() or n == "X"]
    if len(clean) != 10:
        return False
    if "X" in clean[0:9]:
        return False
    if clean[9] == "X":
        clean[9] = 10
    if sum(int(a) * b for a,b in zip(clean,list(range(10,0,-1)))) % 11 == 0:
        return True
    return False
    
print(is_valid("3-598-21508-8"))

isbn = "3-598-2X507-9"
clean = [n for n in isbn if n.isnumeric() or n == "X"]
if "X" in clean[0:9]:
    print("X is not allowed")
print(clean[0:9])
