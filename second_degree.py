import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return a * x ** 2 + b * x + c

def show():
    x = np.arange(-10, 10, 0.1)
    y = f(x)
    plt.plot(x, y)
    plt.grid(True)
    plt.axvline(0, color='k')
    plt.axhline(0, color='k')
    plt.show()

def df(x):
    return 2 * a * x + b

if __name__ == '__main__':
    print("Polynome du second degrée")
    print("f(x) = ax² + bx + c")
    print()
    a = eval(input("a: "))
    b = eval(input("b: "))
    c = eval(input("c: "))
    print(f"f(x) = {a}x² + {b}x + {c}")
    print("Recherche des racines")
    delta = b ** 2 - 4 * a * c
    print(f"Δ  = b² - 4ac = {delta}")
    if delta < 0:
        print("0 solution")
    elif delta == 0:
        print("1 solution double")
    else:
        print("2 solutions")
    if delta >= 0:
        x1 = (-b - np.sqrt(delta)) / (2 * a)
        print(f"x1 = (-b - √Δ) / 2a = {x1}")
        x2 = (-b + np.sqrt(delta)) / (2 * a)
        print(f"x2 = (-b + √Δ) / 2a = {x2}")
    print("Calcul de la dérivée")
    print(f"f'(x) = 2ax + b = {2*a}x + {b}")
    x0 = -b / (2 * a)
    print(f"f'(x)=0, x0 = -b / 2a = {x0}")
    print("Tableau de variation")
    if a > 0:
        print(f"x     | -∞    {x0:.2f}    +∞")
        print(f"f'(x) |    -    |    +")
        print(f"f(x)  |    ↘    |    ↗")
    else:
        print(f"x     | -∞    {x0:.2f}    +∞")
        print(f"f'(x) |    +    |    -")
        print(f"f(x)  |    ↗    |    ↘")
    show()




