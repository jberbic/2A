def hipotenuza (a,b):
    c=(a**2+b**2)**0.5
    print("Katete: ", a,",", b, "; Hipotenuza: ", c)
    print("Katete: {:.0f}, {:.0f}, hipotenuza: {:.3f}".format(a, b, c))

hipotenuza (3,4)
hipotenuza (1,10)
hipotenuza (1,100)
hipotenuza (100,1)
hipotenuza (10,10)
hipotenuza (34,57)
hipotenuza (100000,1050)
hipotenuza (1.5,3.67)
hipotenuza (135.98, 227.15)
