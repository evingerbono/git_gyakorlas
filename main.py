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

print(eredmeny([1,2,8,5],[7,6,10]))
print(eredmeny([1,2,8,5],[4,6,10]))
print(eredmeny([1,2,8,5,10],[4,6,10,]))
print(eredmeny([1,2,8,5,10],[4,6,10,10]))



