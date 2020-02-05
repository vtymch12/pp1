def ile_cyfr(liczba):
    import re
    file = open('dane.txt', 'r')
    suma = 0
    t = file.read()
    li = re.findall('\d+', t)
    for i in li:
        if int(i) in range(100, 99999):
            for j in i:
                if j == liczba:
                    suma +=1
    return suma
ile_cyfr("9")
    
