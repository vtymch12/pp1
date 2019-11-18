import statistics
xyz=[21600,4350,3920,5590,3250,4010]
ss=statistics.mean(xyz)
print(f"Średnią artymetyczną wynosi: {ss}")
mediane=statistics.median(xyz)
print(f"Medianę wynosi: {mediane}")
odchstan=statistics.pstdev(xyz)
print(f"Odchylenie standardowe wynosi:{odchstan}")