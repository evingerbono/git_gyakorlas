"""Megoldás"""

def pontok(lapok):
    pont=0
    for i in range(len(lapok)):
        pont+=lapok[i]
    return pont
def eredmeny(gep_lapok,jatekos_lapok):
    gep_pont=pontok(gep_lapok)
    jatekos_pont=pontok(jatekos_lapok)
    if gep_pont>21 and jatekos_pont>21:
        return "Mindenki vesztett"
    elif gep_pont>21:
        return "A gép vesztett"
    elif jatekos_pont>21:
        return "A játékos vesztett"

"""Tesztestek"""

def teszt_estek():
    #jatekos_vesztett()
    jatekos_egyenlo_lapertek_teszt()
def jatekos_vesztett():
    jatekos=[7, 6, 10]
    gep=[1, 2, 8, 5]
    vart_eredmeny="A játékos vesztett"
    kapott_eredmeny=eredmeny(gep,jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print(f"{vart_eredmeny} teszt sikeres volt.")
    else:
        print(f"{vart_eredmeny} teszt nem volt sikeres.")

def jatekos_egyenlo_lapertek_teszt():
    jatekos = [2,3,5,4,8]
    gep = [10,6,7]
    vart_eredmeny = "A játékos vesztt"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print(f"A játekos egyenlő lapertek teszt sikeres volt.")
    else:
        print(f"A játekos egyenlő lapertek teszt nem volt sikeres.")
def jatekos_lapertek_kisebb_teszt():
    jatekos = [7, 6, 3]
    gep = [1, 2, 8, 6]
    vart_eredmeny = "A játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print(f"A játékos lapérték kisebb teszt sikeres volt.")
    else:
        print(f"A játékos lapérték kisebb teszt nem volt sikeres.")
def gep_lapertek_kisebb_teszt():
    jatekos = [7, 9, 3]
    gep = [5, 2, 8,]
    vart_eredmeny = "A gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print(f"A gép lapérték kisebb teszt sikeres volt.")
    else:
        print(f"A gép lapérték kisebb teszt nem volt sikeres.")
def gep_lapertek_21tobb_teszt():
    jatekos = [7, 6, 3]
    gep = [10, 2, 8, 5]
    vart_eredmeny = "A gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép lapértéke 21 nagyobb teszt sikeres volt.")
    else:
        print("A gép lapértéke 21 nagyobb teszt nem volt sikeres.")

def gep_nyer_teszt():
    jatekos = [7, 6, 4]
    gep = [10, 2, 8]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép nyert mert közeleb van 21 teszt sikeres volt.")
    else:
        print("A gép nyert mert közeleb van 21 teszt  nem volt sikeres.")

def jatekos_nyer():
    jatekos = [7, 6, 6]
    gep = [8, 2, 6]
    vart_eredmeny = "A játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos nyert mert közeleb van 21 teszt sikeres volt.")
    else:
        print("A játékos nyert mert közeleb van 21 teszt  nem volt sikeres.")

def dontetlen_jatekos_nyer_teszt():
    jatekos = [7, 6, 6]
    gep = [8, 2, 2, 7]
    vart_eredmeny = "A játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos nyert mert kevesebb lapja van teszt sikeres volt.")
    else:
        print("A játékos nyert mert kevesebb lapja van teszt  nem volt sikeres.")
def dontetlen_gep_nyer_teszt():
    jatekos = [7, 6, 5]
    gep = [8, 2, 8]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép nyert mert kevesebb lapja van teszt sikeres volt.")
    else:
        print("A gép nyert mert kevesebb lapja van teszt  nem volt sikeres.")
teszt_estek()



