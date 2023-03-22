def pravokutan_trokut (a,b,c):
    if c==(a**2+b**2)**0.5:
        print("Trokut je pravokutan")
    else:
        print("Trokut nije pravokutan")
print("Funkcija pravokutan_trokut")
print("\nStranice: 3,4,5")
pravokutan_trokut (3,4,5)
print("Stranice: 3,4,6")
pravokutan_trokut (3,4,6)
print("Stranice: 1,2,3")
pravokutan_trokut (1,2,3)
print("Stranice: 30,40,50")
pravokutan_trokut (30,40,50)
print("Stranice: 1,2,10")
pravokutan_trokut (1,2,10)

def pravokutan_trokut2 (a,b,c):
    if a+b<c or a+c<b or b+c<a:
        return(print("Nije trokut!!!"))
    if c==(a**2+b**2)**0.5:
        print("Trokut je pravokutan")
    else:
        print("Trokut nije pravokutan")
print("\nFunkcija pravokutan_trokut2")
print("\nStranice: 3,4,5")
pravokutan_trokut2 (3,4,5)
print("Stranice: 3,4,6")
pravokutan_trokut2 (3,4,6)
print("Stranice: 1,2,3")
pravokutan_trokut2 (1,2,3)
print("Stranice: 30,40,50")
pravokutan_trokut2 (30,40,50)
print("Stranice: 1,2,10")
pravokutan_trokut2 (1,2,10)
