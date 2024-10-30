meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7 # stiva LIFO
istoric_comenzi=[]
numar_comenzi=5
numar_tavi=7

while studenti:
    student=studenti.pop(0)
    comanda=comenzi.pop(0)
    istoric_comenzi.append(comanda)
    tavi.pop()
    print(f"{student} a comandat {comanda}")
print("S-a comandat o portie de guias trei portii de ceafa si o portie de papanasi")
print(f"Mai sunt {numar_tavi-numar_comenzi} tavi")
ceafa="ceafa"
papanasi="papanasi"
guias="guias"

if ceafa in meniu:
    print(True)
else:
    print(False)
if papanasi in meniu:
    print(True)
else:
    print(False)
if guias in meniu:
    print(True)
else:
    print(False)

castig_total=preturi[2][1]+3*preturi[1][1]+preturi[0][1]
print(castig_total)
print(f"Produse ce costa cel mult de 7 lei:{preturi[0]} si {preturi[2]}")