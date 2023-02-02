"""Megoldás"""

def pontok(lapok):
    pont=0
    for i in range(len(lapok)):
        pont+=lapok[i]
    return pont
def eredmeny(gep_lapok,jatekos_lapok):
    gelap_db=len(gep_lapok)
    jatekoslap_db=len(jatekos_lapok)
    gep_pont=pontok(gep_lapok)
    jatekos_pont=pontok(jatekos_lapok)
    if gep_pont<=21 and jatekos_pont<=21:
        if jatekos_pont>gep_pont:
            return "A játékos nyert"
        elif jatekos_pont<gep_pont:
            return "A gép nyert"
        elif jatekos_pont==gep_pont:
            if jatekoslap_db<gelap_db:
                return "A játékos nyert"
            elif jatekoslap_db>gelap_db:
                return "A gép nyert"
            else:
                return "Döntetlen osztoztok"
    else:
        if jatekos_pont>21:
            return "A játékos vesztett"
        elif gep_pont>21:
            return "A gép vesztett"
        elif jatekos_pont>21 and gep_pont>21:
            return "Döntetlen a ház nyert"

"""Tesztestek"""

def teszt_estek():
    jatekos_vesztett_teszt()
    jatekos_egyenlo_lapertek_teszt()
    jatekos_lapertek_kisebb_teszt()
    gep_lapertek_kisebb_teszt()
    gep_lapertek_21tobb_teszt()
    gep_nyer_teszt()
    jatekos_nyer_teszt()
    dontetlen_jatekos_nyer_teszt()
    dontetlen_gep_nyer_teszt()
    dontetlen_haz_nyert_teszt()
    dontetlen_osztoznak_teszt()

def jatekos_vesztett_teszt():
    jatekos=[7, 6, 10]
    gep=[1, 2, 8, 5]
    vart_eredmeny="A játékos vesztett"
    kapott_eredmeny=eredmeny(gep,jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print(f"{vart_eredmeny} teszt sikeres volt.")
    else:
        print(f"{vart_eredmeny} teszt nem volt sikeres.")

def jatekos_egyenlo_lapertek_teszt():
    jatekos = [2,8,6]
    gep = [10,6]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print(f"A játekos egyenlő lapertek teszt sikeres volt.")
    else:
        print(f"A játekos egyenlő lapertek teszt nem volt sikeres.")

def jatekos_lapertek_kisebb_teszt():
    jatekos = [7, 6, 3]
    gep = [1, 2, 8, 6]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print(f"A játékos lapérték kisebb teszt sikeres volt.")
    else:
        print(f"A játékos lapérték kisebb teszt nem volt sikeres.")

def gep_lapertek_kisebb_teszt():
    jatekos = [7, 9, 3]
    gep = [5, 2, 8]
    vart_eredmeny = "A játékos nyert"
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

def jatekos_nyer_teszt():
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
    jatekos = [7, 3, 5, 3]
    gep = [8, 2, 8]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép nyert mert kevesebb lapja van teszt sikeres volt.")
    else:
        print("A gép nyert mert kevesebb lapja van teszt  nem volt sikeres.")

def dontetlen_haz_nyert_teszt():
    jatekos = [7, 3, 5, 3, 7]
    gep = [8, 2, 8, 9]
    vart_eredmeny = "Döntetlen a ház nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("Döntetlen a ház nyert teszt sikeres volt.")
    else:
        print("Döntetlen a ház nyert teszt nem volt sikeres.")

def dontetlen_osztoznak_teszt():
    jatekos = [7, 3, 8]
    gep = [8, 2, 8]
    vart_eredmeny = "Döntetlen osztoztok"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("Döntetlen osztoztok teszt sikeres volt.")
    else:
        print("Döntetlen osztoztok teszt nem volt sikeres.")

teszt_estek()



