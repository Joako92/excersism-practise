PhoneNumber = "12234567890"
splitted = PhoneNumber.split()
numbers = [int(word) for word in PhoneNumber.split() if word.isdigit()]

num = []
for c in PhoneNumber:
    if c.isdigit():
        num.append(c)

if PhoneNumber[0] == "1":
    print("starts with 1")
elif PhoneNumber[0] != "1":
    print("Not starts with 1")
##PhoneNumber = PhoneNumber[1:]
print(PhoneNumber[0])
print(num)
print(splitted)
print(numbers)

