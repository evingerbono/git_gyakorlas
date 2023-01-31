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
        return "A gép vesztett."
    elif jatekos_pont>21:
        return "A játékos vesztett."

"""Tesztestek"""

def teszt_estek():
    jatekos_vesztett()
def jatekos_vesztett():
    jatekos=[7, 6, 10]
    gep=[1, 2, 8, 5]
    vart_eredmeny="A játékos vesztett."
    kapott_eredmeny=eredmeny(gep,jatekos)
    if vart_eredmeny==kapott_eredmeny:
        print("Sikeres teszt")
    else:
        print("A teszt nem sikerült")

teszt_estek()



