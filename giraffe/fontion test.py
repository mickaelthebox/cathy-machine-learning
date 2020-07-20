


# Test de fontions
def moyenne():
    a = False
    note = input("entrer vos notes:")
    note = float
    while a == False :
        note = note + i
        i = [i+1]
        t+=1
    moyenne= note/len(t)
    return moyenne


def moyenne2(list):
    longueur = len(list)
    sum = 0 
    i = 0
    for i in range(longueur):
        sum += list[i]
    return sum/longueur


print(moyenne2([5,10]))