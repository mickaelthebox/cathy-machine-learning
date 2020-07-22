# fonction pour voir quel est le plus grand entre l'energie limite et l'enerve potentiel
def ep (m,h,el,g=9.8):
    E=m*h*g
    if E<el:
        print ("le plus grand est : el")
    else:
        print ("le plus grand est : E")

ep(3,4,5)

#fontion fibonaci 0 1 1 2 3 5 8 13

def fibonaci(n):
    for i in range(0,n,):
        j= 1
        i = i + j
        j=i
    return fibonaci

