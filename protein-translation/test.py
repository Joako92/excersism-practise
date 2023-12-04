value = "AUGUUUUGG"
lista = list(value)
c_1 = "".join(lista[0:3])
c_2 = "".join(lista[3:6])
c_3 = "".join(lista[6:9])
result = [c_1, c_2, c_3]

print(lista)
print(result)
for r in result:
    print(r)
