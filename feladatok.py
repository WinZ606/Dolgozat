def feladat1():
    szam1 = int(input("Kérek egy páros számot: "))
    if szam1 % 2 == 0:
        return szam1
    else:
        while szam1 % 2 != 0:
            szam1 = int(input("Kérek egy PÁROS számot: "))
        return szam1
