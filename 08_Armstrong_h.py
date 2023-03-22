def armstrong (n):
    if not (n//100>0 and n//100<10):
        return (print("Broj {:.0f} nije troznamenkast!".format(n)))
    #if n//100<1 or n//100>9 #2.način
    #if len(str(n))==3 #3.način
    j = n%10
    d = n//10%10
    s = n//10//10
    if n==s**3+d**3+j**3:
        print("Broj {:.0f} je Armstrongov".format(n))
    else:
        print("Broj {:.0f} nije Armstrongov".format(n))

armstrong (153)
armstrong (370)
armstrong (371)
armstrong (407)
armstrong (100)
armstrong (555)
armstrong (907)
armstrong (670)
armstrong (3704)
armstrong (58)








    
