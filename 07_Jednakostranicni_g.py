def jednakostranicni (a):
    v = (3*a**2/4)**0.5
    P = a*v/2

    print("Stranica a={:.3f}, površina je P={:.3f}".format(a,P))

jednakostranicni(10)
jednakostranicni(100)
jednakostranicni(1034.34209)
jednakostranicni(304920349.03940394)
jednakostranicni(2323.43)

