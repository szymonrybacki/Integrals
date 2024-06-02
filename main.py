import math
import random
from algorythms import ractangleMethod
from algorythms import trapezeMethod
from algorythms import simpsonMethod

a = random.randint(1, 10)
b = random.randint(1, 10)
h = (a - b) ** 2 / (a + b) ** 2

# Obliczanie pól
circleFunction = lambda x : math.sqrt(1 - x * x)
uFunc = lambda x : x * x
elipseFunc = lambda x : math.sqrt(1 - x * x / (a * a)) * b
sinFunc = lambda x : math.sin(x)

print("obliczenie pól")

# S1, Koło o promieniu 1  
rec = ractangleMethod.RactangleMethod(-1, 1, 100000)
trap = trapezeMethod.TrapezeMethod(-1, 1, 100000)
simp = simpsonMethod.SimpsonMethod(-1, 1, 100000)

print(rec.calculateIntegral(circleFunction) *2) # *2 bo to połowa koła
print(trap.calculateIntegral(circleFunction) *2)
print(simp.calculateIntegral(circleFunction) *2)
print(math.pi) # taki powinien wyjść wynik

# S2, Funkcja x^2
rec = ractangleMethod.RactangleMethod(0, 1, 100000)
trap = trapezeMethod.TrapezeMethod(0, 1, 100000)
simp = simpsonMethod.SimpsonMethod(0, 1, 100000)

print(rec.calculateIntegral(uFunc))
print(trap.calculateIntegral(uFunc))
print(simp.calculateIntegral(uFunc))

# S3, Elipsa o parametrach a, b
rec = ractangleMethod.RactangleMethod(-a, a, 100000)
trap = trapezeMethod.TrapezeMethod(-a, a, 100000)
simp = simpsonMethod.SimpsonMethod(-a, a, 100000)


print(rec.calculateIntegral(elipseFunc) * 2)
print(trap.calculateIntegral(elipseFunc) * 2)
print(simp.calculateIntegral(elipseFunc) * 2)
print(a*b*math.pi) # taki powinien wyjść wynik

# S4, Funkcja sin(x)
rec = ractangleMethod.RactangleMethod(0, math.pi, 100000)
trap = trapezeMethod.TrapezeMethod(0, math.pi, 100000)
simp = simpsonMethod.SimpsonMethod(0, math.pi, 100000)

print(rec.calculateIntegral(sinFunc))
print(trap.calculateIntegral(sinFunc))
print(simp.calculateIntegral(sinFunc))

# Obliczanie długości

print("obliczenie długości")

circleDerivative = lambda x: 0 if (1 - x * x == 0) else (-x / math.sqrt(1 - x * x))
elipseDerivative = lambda x: 0 if (1 - x * x / (a * a) == 0) else -((b * x) / (a * a * math.sqrt(1 - (x * x) / (a * a))))
sinDerevative = lambda x: math.cos(x)
                                                        
circleFunc2 = lambda x: math.sqrt(1 + circleDerivative(x) ** 2)
elipseFunc2 = lambda x: math.sqrt(1 + elipseDerivative(x) ** 2)
sinFunc2 = lambda x: math.sqrt(1 + sinDerevative(x) ** 2)

# L1, Koło o promieniu 1
rec = ractangleMethod.RactangleMethod(-1, 1, 100000) # puścić dla większej ilości
trap = trapezeMethod.TrapezeMethod(-1, 1, 100000)
simp = simpsonMethod.SimpsonMethod(-1, 1, 100000)

print(rec.calculateIntegral(circleFunc2))
print(trap.calculateIntegral(circleFunc2))
print(simp.calculateIntegral(circleFunc2))
print(math.pi)

# L2, Elipsa o parametrach a, b
expValue = math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
rec = ractangleMethod.RactangleMethod(-a, a, 100000) # puścić dla większej ilości
trap = trapezeMethod.TrapezeMethod(-a, a, 100000)
simp = simpsonMethod.SimpsonMethod(-a, a, 100000)

print(rec.calculateIntegral(elipseFunc2) * 2)
print(trap.calculateIntegral(elipseFunc2) * 2)
print(simp.calculateIntegral(elipseFunc2) * 2)
print(expValue)

#L3, Funkcja sin(x)
rec = ractangleMethod.RactangleMethod(0, 2*math.pi, 100000)
trap = trapezeMethod.TrapezeMethod(0, 2*math.pi, 100000)
simp = simpsonMethod.SimpsonMethod(0, 2*math.pi, 100000)

print(rec.calculateIntegral(sinFunc2))
print(trap.calculateIntegral(sinFunc2))
print(simp.calculateIntegral(sinFunc2))
print('7.6404') # taki powinien wyjść wynik