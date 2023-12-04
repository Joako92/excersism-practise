orbita_n = []
valores = mayor = 0

number = int(input("Ingrese un numero:_"))
if number < 1:
    raise ValueError("Solo enteros positivos.")
primero = number
while number != 1:
    orbita_n.append(number)
    valores += number
    if number % 2 == 0:
        number = number // 2
    else:
        number = (number * 3) + 1
    if number > mayor:
        mayor = number

valores += number
orbita_n.append(number)
prom = round(valores / len(orbita_n), 1)

print("Numero:", primero)
print("Orbita de N:", orbita_n)
print("Longitud de la órbita:", len(orbita_n))
print("Promedio de todos los valores de la órbita:", prom)
print("Mayor de los números en esa órbita:", mayor)
