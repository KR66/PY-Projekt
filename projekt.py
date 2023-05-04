with open("projekt.txt","r",encoding="utf-8") as billentyuk:
    billentyu = [b.strip().split(";") for b in billentyuk]

b_szama = 0
for item in billentyu:
    b_szama = b_szama + 1
print(f"A billentyűk száma: {b_szama} db")

ba_szama = 0
for item in billentyu:
    ba_szama = ba_szama + 1
print(f"A billentyű árak száma: {ba_szama} db")

b_osszeg = sum(int(b) in billentyu)
print(f"A billentyű árak összege: {b_osszeg} Ft")


# # Objektum Orientáltan
class Project:
    def __init__(self,nev,ar):
        self.nev = nev
        self.ar = ar
projekt_lista = []

billentyuk = open("projekt.txt","r",encoding="utf-8")
for sor in billentyuk:
    oszlop = sor.strip().split(";")
    projekt_lista.append(Project(oszlop[0],int(oszlop[1])))

legdragabb = max(b.ar for b in projekt_lista)
for item in projekt_lista:
    if item.ar == legdragabb:
        print(f"A legdrágább billentyű: {item.nev}")

legolcsobb = min(b.ar for b in projekt_lista)
for item in projekt_lista:
    if item.ar == legolcsobb:
        print(f"A legolcsóbb billentyű: {item.nev}")

lista = ["HP Happy Hacking","Optimus Popular","Apple Magic Keyboard iPad Pro 11","Glorious PC Gaming Race GMMK Pro","Razer Huntsman V2 Analog","ASUS ROG Claymore II","Razer Deathstalker V2 Pro","Corsair K100 AIR","Keychron Q4 QMK TKL","SteelSeries Apex Pro"]
for i in range(10):
    print(lista[i])