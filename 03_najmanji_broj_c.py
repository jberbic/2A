def Najmanji(a,b,c):
    mnm=a
    if b<c:
        if b<a:
            mnm=b
    else:
        if c<a:
            mnm=c
    print("Najmanji od triju: ", mnm)


print("#1. 10,20,30"), Najmanji(10,20,30)
print("#1. 20,10,30"), Najmanji(20,10,30)
print("#1. 0.01,2.12,3.13"), Najmanji(0.1,2.12,3.13)
print("#1. 2.12,0.1,3.13"), Najmanji(2.12,0.01,3.13)  
