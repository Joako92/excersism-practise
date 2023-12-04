a = "GGACGGATTCTG"
b = "AGGACGGATTCT"

## SI SON IGUALES CONTINUA, SI ENCUENTRA DIFERENCIA SUMA 1
diff = 0
counter = 0
for n in list(a):
    if n == list(b)[counter]:
        counter += 1
        continue
    else:
        diff += 1
        counter += 1
        continue
print(diff)
