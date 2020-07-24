def fibonaci(n):
    a = 0
    b = 1
    while a < n:
        print (a)
        a, b = b, a+b

# return list
fi = []
def fiboo(n):
    c = 0
    d = 1
    while c < n:
        fi.append(c)
        c,d = d, c+d
    print (fi)

fiboo(10)