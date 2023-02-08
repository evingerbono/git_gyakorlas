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
        if jatekos_pont>21 and gep_pont>21:
            return "Döntetlen a ház nyert"
        elif jatekos_pont>21:
            return "A játékos vesztett"
        elif gep_pont>21:
            return "A gép vesztett"

"""Tesztestek"""

def teszt_estek():
    jatekos_egyenlo_lapertek_teszt()
    jatekos_lapertek_kisebb_teszt()
    gep_lapertek_kisebb_teszt()
    dontetlen_jatekos_nyer_teszt()
    dontetlen_gep_nyer_teszt()
    jatekos_nyer_19_kevesebb_lap_teszt()
    jatekos_nyer_19_tobb_lap_teszt()
    jatekos_nyer_21_teszt()
    jatekos_vesztett_21_tobb_teszt()
    jatekos_veszit_19_kevesebb_lap_teszt()
    jatekos_veszit_19_tob_lap_teszt()
    gep_nyer_19_kevesebb_lap_teszt()
    gep_nyer_19_tobb_lap_teszt()
    gep_nyer_21_teszt()
    gep_lapertek_21tobb_teszt()
    gep_veszit_19_kevesebb_lap_teszt()
    gep_veszit_19_tobb_lap_teszt()
    dontetlen_osztoznak_pont_21_teszt()
    dontetlen_egyforma_pontjuk_21_kevesebb_teszt()
    dontetlen_haz_nyert_teszt()

def jatekos_vesztett_21_tobb_teszt():
    jatekos=[7, 6, 10]
    gep=[1, 2, 8, 5]
    vart_eredmeny="A játékos vesztett"
    kapott_eredmeny=eredmeny(gep,jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos lapértéke 21 nagyobb teszt sikeres volt.")
    else:
        print("A játékos lapértéke 21 nagyobb teszt nem volt sikeres.")

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

def gep_nyer_21_teszt():
    jatekos = [7, 6, 4]
    gep = [10, 3, 8]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép nyert mert 21 van teszt sikeres volt.")
    else:
        print("A gép nyert mert 21 van teszt  nem volt sikeres.")

def jatekos_nyer_21_teszt():
    jatekos = [7, 6, 8]
    gep = [8, 2, 6]
    vart_eredmeny = "A játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos nyert mert 21 van teszt sikeres volt.")
    else:
        print("A játékos nyert mert 21 van teszt  nem volt sikeres.")

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
    jatekos = [7, 3, 2, 10]
    gep = [8, 2, 8, 4]
    vart_eredmeny = "Döntetlen a ház nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("Döntetlen a ház nyert teszt sikeres volt.")
    else:
        print("Döntetlen a ház nyert teszt nem volt sikeres.")

def dontetlen_osztoznak_pont_21_teszt():
    jatekos = [10, 2, 9]
    gep = [9, 4, 8]
    vart_eredmeny = "Döntetlen osztoztok"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("Döntetlen osztoznak, mert mindenkinek 21-pontja van teszt sikeres volt.")
    else:
        print("Döntetlen osztoznak, mert mindenkinek 21-pontja van teszt nem volt sikeres.")

def dontetlen_egyforma_pontjuk_21_kevesebb_teszt():
    jatekos = [10, 2, 7]
    gep = [9, 4, 6]
    vart_eredmeny = "Döntetlen osztoztok"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("Döntetlen osztoznak, mert egyforma pontjuk van teszt sikeres volt.")
    else:
        print("Döntetlen osztoznak, mert egyforma pontjuk van teszt nem volt sikeres.")

def jatekos_nyer_19_kevesebb_lap_teszt():
    jatekos = [7, 6, 6]
    gep = [8, 2, 5, 4]
    vart_eredmeny = "A játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos nyert 19-ponttal, mert kevesebb lapja van teszt sikeres volt.")
    else:
        print("A játékos nyert 19-ponttal, mert kevesebb lapja van teszt nem volt sikeres.")

def gep_nyer_19_kevesebb_lap_teszt():
    jatekos = [7, 4, 3, 2, 3]
    gep = [8, 2, 5, 4]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép nyert 19-ponttal, mert kevesebb lapja van teszt sikeres volt.")
    else:
        print("A gép nyert 19-ponttal, mert kevesebb lapja van teszt nem volt sikeres.")

def jatekos_nyer_19_tobb_lap_teszt():
    jatekos = [7, 4, 3, 2, 3]
    gep = [8, 2, 5, 2]
    vart_eredmeny = "A játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos nyert 19-ponttal teszt sikeres volt.")
    else:
        print("A játékos nyert 19-ponttal teszt nem volt sikeres.")

def gep_nyer_19_tobb_lap_teszt():
    jatekos = [7, 4, 6]
    gep = [8, 2, 5, 4]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép nyert 19-ponttal teszt sikeres volt.")
    else:
        print("A gép nyert 19-ponttal tszt nem volt sikeres.")

def jatekos_veszit_19_kevesebb_lap_teszt():
    jatekos = [7, 6, 6]
    gep = [8, 2, 5, 5]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos veszít 19-ponttal teszt sikeres volt.")
    else:
        print("A játékos veszít 19-ponttal teszt nem volt sikeres.")

def gep_veszit_19_kevesebb_lap_teszt():
    jatekos = [10, 1, 5, 5]
    gep = [8, 2, 9]
    vart_eredmeny = "A játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép veszít 19-ponttal teszt sikeres volt.")
    else:
        print("A gép veszít 19-ponttal teszt nem volt sikeres.")

def jatekos_veszit_19_tob_lap_teszt():
    jatekos = [7, 6, 2, 4]
    gep = [8, 2, 9]
    vart_eredmeny = "A gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos veszít 19-ponttal, de több lappal teszt sikeres volt.")
    else:
        print("A játékos veszít 19-ponttal, de több lappal teszt nem volt sikeres.")

def gep_veszit_19_tobb_lap_teszt():
    jatekos = [7, 6, 6]
    gep = [8, 2, 4, 5]
    vart_eredmeny = "A játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép veszít 19-ponttal, de több lappal teszt sikeres volt.")
    else:
        print("A gép veszít 19-ponttal, de több lappal teszt nem volt sikeres.")


teszt_estek()



