inventaire = {
    "bananes" : 50,
    "pommes" : 30,
    "cerise" : 40
}

inventaire.keys()
inventaire.values()

# devoirs
classeur = {
    "positif" : [],
    "negatif" : [],
}
def trier(classeur,nombre):
    if nombre < 0:
        classeur["positiif"] = nombre
    else:
        classeur["negatif"] = nombre
    return classeur
