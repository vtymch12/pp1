wzrost=int(input("podaj wzrost w cm "))
wage=int(input("podaj wage w kg "))
bmi=wage/((wzrost/100)**2)
if bmi<18.5:
    print(f"wskaznik bmi {bmi} (niedowaga)")
elif bmi<=24.9:
    print(f"wskaznik bmi {bmi} (prawidlowa)")
elif bmi<=29.9:
    print(f"wskaznik bmi {bmi} (nadwaga)")
else:
    print(f"wskaznik bmi {bmi} (otylosc)")