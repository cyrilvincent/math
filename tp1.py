# Faire la factorielle de n
# Calculer le nieme element de la suite de fibonacci
#   a=0 b=1 f(2)=a+b=1 f(3)=f(2)+f(1)=1+1=2 f(4)=f(3)+f(2)=2+1=3 f(n)=f(n-1)+f(n-2) avec f(0)=0 et f(1)=1

n=15
a=0
b=1
result = 0
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(2, n+1):
        result = a + b
        a = b
        b = result
    print(result)
