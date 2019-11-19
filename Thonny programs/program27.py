a = int(input("Podaj pierwszą liczbę całkowitą dodatnią: "))
b = int(input("Podaj drugą liczbę całkowitą dodatnią: "))
def NWD(a, b):
    c = 0
    while b != 0:
        c = a % b
        print("a = {a}; b = {b}".format(a = a, b = b))
        a, b = b, c
    print("a = {a}; b = {b}".format(a = a, b = b))
