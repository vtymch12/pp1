import random
kostok=random.randint(1,6)
x=int(input(" Podaj, ile oczek kostki wyrzucił komputer:"))
if x>6:
    print("Nie mozesz wywodzic czyyslo wieeksze od  6")
print( "Komputer wyrzucił:",kostok)
if x==kostok:
    print("Zgadłeś")
else:
    print("Nie Zgadłeś")
    
