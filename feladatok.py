import random

def feladat1():
    szam1 = int(input("Kérek egy páros számot: "))
    if szam1 % 2 == 0:
        return szam1
    else:
        while szam1 % 2 != 0:
            szam1 = int(input("Ez nem páros! PÁROS számot kérek! "))

def feladat2():
    szamok = []
    i = 0
    o = 0
    harommal = 0
    while i < 13:
        szam = int(random.random()*151)+10
        szamok.append(szam)
        i += 1
    print(szamok)
    while o < 13:
        if szamok[o] % 3 == 0:
            harommal += 1
        o += 1
    print(f"A számok között {harommal}db 3-mal osztható van!")

def feladat3(text,N):
    text = text.upper()
    if len(text) < N:
        print(f"Nincs {N}. karakter!")
    print(text[(N-1)]*3)

def feladat4():
    nevek = ""
    nevekszam = 0
    while nevek != "@":
        nevek = str(input("Kérek neveket: "))
        nevekszam += 1
    return nevekszam

