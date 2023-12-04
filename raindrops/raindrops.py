def convert(number):
    r_list = []
    index = [3,5,7]
    for i in index:
        t =(number % i)
        if t == 0:
            if i == 3:
                r_list.append("Pling")
            elif i == 5:
                r_list.append("Plang")
            elif i == 7:
                r_list.append("Plong")

    if r_list == []:
        r_list.append(str(number))
               
    result = "".join(r_list)
    return result

