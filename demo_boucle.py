# i = 0
# while i < 10:
#     print(i)
#     # i += 1

# for i in range(10):
#     print(i)
#     if i == 8:
#         break

result = 1
for i in range(1,11):
    result *= i
print(result)

for i in range(11):
    for j in range(11):
        print(f"{i}*{j}={i*j}")

# TP
# Calculer la factorielle de n qui est une variable >= 1
# Calculer la suite de fibonacci pour n > 1
# f(n) = f(n-1) + f(n-2) avec f(0)=0 et f(1)=1
# BONUS: n>1 dire si est est premier ou non

n=5
result = 1
for i in range(2, n+1):
    result *= i
print(f"{n}!={result}")

f0=0
f1=1
n=10
for i in range(2, n+1):
    result = f0 + f1
    f0=f1
    f1=result
print(f"F({n})={result}")

n=1223
if n<=1:
    print("Non premier")
else:
    for div in range(2, n):
        if n % div == 0:
            print("Non premier")
            break
    print("Premier")




