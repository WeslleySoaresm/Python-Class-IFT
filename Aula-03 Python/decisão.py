#decisão
numero = input("Digite um número: ")
if int(numero) > 0:
    print(f"O número {numero} é positivo.")
elif int(numero) < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"O número {numero} é zero.")
# Verifica se o número é par ou ímpar
if int(numero) % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
# Verifica se o número é primo
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
if is_prime(int(numero)):
    print(f"O número {numero} é primo.")
else:
    print(f"O número {numero} não é primo.")
# Verifica se o número é um quadrado perfeito
def is_perfect_square(n):
    return int(n**0.5) ** 2 == n
if is_perfect_square(int(numero)):
    print(f"O número {numero} é um quadrado perfeito.")
else:
    print(f"O número {numero} não é um quadrado perfeito.")
# Verifica se o número é um cubo perfeito
def is_perfect_cube(n):
    return int(n**(1/3)) ** 3 == n
if is_perfect_cube(int(numero)):            
    print(f"O número {numero} é um cubo perfeito.")
else:
    print(f"O número {numero} não é um cubo perfeito.")
# Verifica se o número é um número de Fibonacci
def is_fibonacci(n):
    a, b = 0, 1
    while a < n:
        a, b = b, a + b
    return a == n
if is_fibonacci(int(numero)):
    print(f"O número {numero} é um número de Fibonacci.")
else:
    print(f"O número {numero} não é um número de Fibonacci.")
# Verifica se o número é um número Armstrong
def is_armstrong(n):                
    digits = [int(d) for d in str(n)]
    return sum(d ** len(digits) for d in digits) == n
if is_armstrong(int(numero)):
    print(f"O número {numero} é um número Armstrong.")
else:
    print(f"O número {numero} não é um número Armstrong.")
# Verifica se o número é um número perfeito
def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)
if is_perfect(int(numero)):
    print(f"O número {numero} é um número perfeito.")
else:
    print(f"O número {numero} não é um número perfeito.")
# Verifica se o número é um número abundante
def is_abundant(n):     
    return n < sum(i for i in range(1, n) if n % i == 0)
if is_abundant(int(numero)):
    print(f"O número {numero} é um número abundante.")
else:
    print(f"O número {numero} não é um número abundante.")
# Verifica se o número é um número deficiente
def is_deficient(n):
    return n > sum(i for i in range(1, n) if n % i == 0)
if is_deficient(int(numero)):
    print(f"O número {numero} é um número deficiente.")
else:
    print(f"O número {numero} não é um número deficiente.")
# Verifica se o número é um número feliz
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1
if is_happy(int(numero)):
    print(f"O número {numero} é um número feliz.")
else:
    print(f"O número {numero} não é um número feliz.")
# Verifica se o número é um número triste
def is_sad(n):
    return not is_happy(n)
if is_sad(int(numero)):
    print(f"O número {numero} é um número triste.")
else:
    print(f"O número {numero} não é um número triste.")
# Verifica se o número é um número triangular
def is_triangular(n):
    x = (8 * n + 1) ** 0.5
    return x.is_integer() and (x - 1) % 2 == 0
if is_triangular(int(numero)):
    print(f"O número {numero} é um número triangular.")
else:
    print(f"O número {numero} não é um número triangular.")
# Verifica se o número é um número pentagonal
def is_pentagonal(n):
    x = (1 + (1 + 24 * n) ** 0.5) / 6
    return x.is_integer()
if is_pentagonal(int(numero)):
    print(f"O número {numero} é um número pentagonal.")
else:
    print(f"O número {numero} não é um número pentagonal.")
# Verifica se o número é um número hexagonal                                            
def is_hexagonal(n):
    x = (1 + (1 + 8 * n) ** 0.5) / 4
    return x.is_integer()
if is_hexagonal(int(numero)):
    print(f"O número {numero} é um número hexagonal.")
else:
    print(f"O número {numero} não é um número hexagonal.")
# Verifica se o número é um número octagonal
def is_octagonal(n):
    x = (3 + (3 + 8 * n) ** 0.5) / 2
    return x.is_integer()
if is_octagonal(int(numero)):
    print(f"O número {numero} é um número octagonal.")
else:
    print(f"O número {numero} não é um número octagonal.")
# Verifica se o número é um número heptagonal
def is_heptagonal(n):
    x = (5 + (5 + 24 * n) ** 0.5) / 10
    return x.is_integer()
if is_heptagonal(int(numero)):              
    print(f"O número {numero} é um número heptagonal.")
else:
    print(f"O número {numero} não é um número heptagonal.")