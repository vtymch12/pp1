tablica = [1,2,3,4,5,6,7,8,9]
def suma_parzyste(tablica):
    suma=0
    for i in tablica:
        if i%2==0:
            suma+=i
    return suma
print(suma_parzyste(tablica))