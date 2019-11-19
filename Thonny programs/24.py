x=int(input("Podaj ocenę:"))
for x in range(1,6):
    if x==1:
        print(" Ocena słownie:niedostateczny")
        break
        continue
    elif x==2:
        print(" Ocena słownie:mierny")
    elif x==3:
        print(" Ocena słownie:dostateczny")
    elif x==4:
        print(" Ocena słownie:dobry")
    elif x==5:
        print(" Ocena słownie:bardzo dobry")
    elif x==6:
        print(" Ocena słownie:celujący")
    else:
        print("Wpisz prawidlowe liczbe")
