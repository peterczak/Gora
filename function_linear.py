import math
import matplotlib.pyplot as plt
def mat_funkcja(x):
    return pow(x, 3) - 1500000 * pow(x, 2) + 750000000002 * x - 125000000000999990
def mat_funkcja2(i):
    return [pow(x, 3) - 1500000 * pow(x, 2) + 750000000002 * x - 125000000000999990 for x in i]

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
            x = range(int(a),int(c))
            plt.plot(x, mat_funkcja2(x))
            plt.show()
        else:
            a = c
            x = range(int(c),int(b))
            plt.plot(x, mat_funkcja2(x))
            plt.show()

    print("Wartość pierwiastka wynosi : ", "%.5f" % c)
bisection(0, pow(10,6), 0.01)
x = range(0, pow(10,6))
plt.plot(x, mat_funkcja2(x))
plt.show()