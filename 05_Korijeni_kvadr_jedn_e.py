def korijeni_kvadr_jedn (a,b,c):
    x1 = (-b+(b**2-4*a*c)**0.5)/(2*a)
    x2 = (-b-(b**2-4*a*c)**0.5)/(2*a)
    print(x1,x2)

korijeni_kvadr_jedn(1,-4,4)
korijeni_kvadr_jedn(1,1,-2)
korijeni_kvadr_jedn(1,-2,11)
