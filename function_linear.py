import math
def mat_funkcja(x):
    return pow(x, 3) - 1500000 * pow(x, 2) + 750000000002 * x - 125000000000999990

def bisection(a, b, epsilon):
    if (mat_funkcja(a) * mat_funkcja(b) >= 0):
        print("Podane punkty nie spełniają założen funcji, tzn przyjmuje różne znaki na końcach przedziału")
        return
    while (abs(b - a) >= epsilon):
        c = (a + b) / 2         # Znajduje srodkowy element przedziału
        if (abs(mat_funkcja(c)) <= epsilon): #jesli wartosc srodkowewgo elementu jest miejscem zerowym (przyblizenie epsilon)
            break
        # Ktora obszar ma teraz wybrac [a,c] czy [b,c]
        elif (mat_funkcja(c) * mat_funkcja(a) < 0): # sprawdzanie tego samego zalozenia co w 6 linii
            b = c
        else:
            a = c

    print("Wartość pierwiastka wynosi : ", "%.5f" % c)
bisection(0, pow(10,6), 0.01)