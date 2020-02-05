def suma_duplikatow(tablica):
    dup = []
    for i in range(len(tablica)):
        for j in range(len(tablica)):
            if i!=j:
                if tablica[i]==tablica[j]:
                    dup.append(tablica[i])
                    break
    
    return sum(dup)

suma_duplikatow([2,3,4,2,5,3])
    