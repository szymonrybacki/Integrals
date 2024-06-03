import sys
sys.path.append("..")
from algorythms import ractangleMethod
from algorythms import trapezeMethod
from algorythms import simpsonMethod
import math
import random
import matplotlib.pyplot as plt
#S1
#Estymacja PI na podstawie obliczania pola kola o promieniu 1
#Liczba PI 3,141592653589793
#Testy wykonane dla liczby n z zakresu 100 000 do 5 000 000, z iteracja co 100 000
print('S1')
circleFunction = lambda x : math.sqrt(1 - x * x)

# # #Algorytm A1
s1a1Table = []

for i in range(100000, 5000000, 100000):
    rec = ractangleMethod.RactangleMethod(-1, 1, i)
    out = abs(math.pi - rec.calculateIntegral(circleFunction) * 2)
    s1a1Table.append(out)

# #Algorytm A2
s1a2Table = []
for i in range(100000, 5000000, 100000):
    trap = trapezeMethod.TrapezeMethod(-1, 1, i)
    out = abs(math.pi - trap.calculateIntegral(circleFunction) * 2)
    s1a2Table.append(out)

# #Algorytm A3
s1a3Table = []
for i in range(100000, 5000000, 100000):
    simp = simpsonMethod.SimpsonMethod(-1, 1, i)
    out = abs(math.pi - simp.calculateIntegral(circleFunction) * 2)
    s1a3Table.append(out)

print(sum(s1a1Table))
print('==================')
print(sum(s1a2Table))
print('==================')
print(sum(s1a3Table))


# #S2
# #Parabola na przedziale <0, 1>
print('S2')
uFunc = lambda x : x * x

# #Algorytm A1
s2a1Table = []
for i in range(100000, 5000000, 100000):
    rec = ractangleMethod.RactangleMethod(0, 1, i)
    out = abs(1/3 - rec.calculateIntegral(uFunc))
    s2a1Table.append(out)

#Algorytm A2
s2a2Table = []
for i in range(100000, 5000000, 100000):
    trap = trapezeMethod.TrapezeMethod(0, 1, i)
    out = abs(1/3 - trap.calculateIntegral(uFunc))
    s2a2Table.append(out)

# #Algorytm A3
s2a3Table = []
for i in range(100000, 5000000, 100000):
    simp = simpsonMethod.SimpsonMethod(0, 1, i)
    out = abs(1/3 - simp.calculateIntegral(uFunc))
    s2a3Table.append(out)

print(sum(s2a1Table)) 
print('==================')
print(sum(s2a2Table))
print('==================')
print(sum(s2a3Table))

print('S3')
# # #S3
# # #Elipsa o parametrach a, b
elipseFunc = lambda x : math.sqrt(1 - x * x / (a * a)) * b

s3a1Table = []
s3a2Table = []
s3a3Table = []
# # for i in range(1, 4):
a = random.randint(1, 10)
b = random.randint(1, 10)

print(a, b)

for j in range(100000, 5000000, 100000):
    rec = ractangleMethod.RactangleMethod(-a, a, j)
    out = abs(a*b*math.pi - rec.calculateIntegral(elipseFunc) * 2)
    s3a1Table.append(out)
for j in range(100000, 5000000, 100000):
    trap = trapezeMethod.TrapezeMethod(-a, a, j)
    out = abs(a*b*math.pi - trap.calculateIntegral(elipseFunc) * 2)
    s3a2Table.append(out)
for i in range(100000, 5000000, 100000):
    simp = simpsonMethod.SimpsonMethod(-a, a, i)
    out = abs(a*b*math.pi - simp.calculateIntegral(elipseFunc) * 2)
    s3a3Table.append(out)

print(sum(s3a1Table))
print('==================')
print(sum(s3a2Table))
print('==================')
print(sum(s3a3Table))

print('S4')
# # #S4
# # #Funkcja sin(x)
sinFunc = lambda x : math.sin(x)

s4a1Table = []
s4a2Table = []
s4a3Table = []
for i in range(100000, 5000000, 100000):
    rec = ractangleMethod.RactangleMethod(0, math.pi, i)
    out = abs(2 - rec.calculateIntegral(sinFunc))
    s4a1Table.append(out)

for i in range(100000, 5000000, 100000):
    trap = trapezeMethod.TrapezeMethod(0, math.pi, i)
    out = abs(2 - trap.calculateIntegral(sinFunc))
    s4a2Table.append(out)

for i in range(100000, 5000000, 100000):
    simp = simpsonMethod.SimpsonMethod(0, math.pi, i)
    out = abs(2 - simp.calculateIntegral(sinFunc))
    s4a3Table.append(out)

print(sum(s4a1Table))
print('==================')
print(sum(s4a2Table))
print('==================')
print(sum(s4a3Table))

print('L1')
# #L1
# #Obwód koła o promieniu 1
circleDerivative = lambda x: 0 if (1 - x * x == 0) else (-x / math.sqrt(1 - x * x))                                                     
circleFunc2 = lambda x: math.sqrt(1 + circleDerivative(x) ** 2)

l1a1Table = []
l1a2Table = []
l1a3Table = []

for i in range(100000, 5000000, 100000):
    rec = ractangleMethod.RactangleMethod(-1, 1, i)
    out = abs(math.pi - rec.calculateIntegral(circleFunc2))
    l1a1Table.append(out)

for i in range(100000, 5000000, 100000):
    trap = trapezeMethod.TrapezeMethod(-1, 1, i)
    out = abs(math.pi - trap.calculateIntegral(circleFunc2))
    l1a2Table.append(out)

for i in range(100000, 5000000, 100000):
    simp = simpsonMethod.SimpsonMethod(-1, 1, i)
    out = abs(math.pi - simp.calculateIntegral(circleFunc2))
    l1a3Table.append(out)

print(sum(l1a1Table))
print('==================')
print(sum(l1a2Table))
print('==================')
print(sum(l1a3Table))

print('L2')
# # # #L2
# # # #Obwód elipsy o parametrach a, b
elipseDerivative = lambda x: 0 if (1 - x * x / (a * a) == 0) else -((b * x) / (a * a * math.sqrt(1 - (x * x) / (a * a))))                                             
elipseFunc2 = lambda x: math.sqrt(1 + elipseDerivative(x) ** 2)

l2a1Table = []
l2a2Table = []
l2a3Table = []

a = random.randint(1, 10)
b = random.randint(1, 10)
h = (a - b) ** 2 / (a + b) ** 2

print(a, b, h)

expValue = math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))


for j in range(100000, 5000000, 100000):
    rec = ractangleMethod.RactangleMethod(-a, a, j)
    out = abs(expValue - rec.calculateIntegral(elipseFunc2) * 2)
    l2a1Table.append(out)
for j in range(100000, 5000000, 100000):
    trap = trapezeMethod.TrapezeMethod(-a, a, j)
    out = abs(expValue - trap.calculateIntegral(elipseFunc2) * 2)
    l2a2Table.append(out)
for i in range(100000, 5000000, 100000):
    simp = simpsonMethod.SimpsonMethod(-a, a, i)
    out = abs(expValue - simp.calculateIntegral(elipseFunc2) * 2)
    l2a3Table.append(out)

print(sum(l2a1Table))
print('==================')
print(sum(l2a2Table))
print('==================')
print(sum(l2a3Table))

print('L3')
# # #L3
# # #Długość krzywej sinus na przedziale [0, 2*pi]
sinDerevative = lambda x: math.cos(x)
sinFunc2 = lambda x: math.sqrt(1 + sinDerevative(x) ** 2)

l3a1Table = []
l3a2Table = []
l3a3Table = []

for i in range(100000, 5000000, 100000):
    rec = ractangleMethod.RactangleMethod(0, 2*math.pi, i)
    out = abs(7.6404 - rec.calculateIntegral(sinFunc2))
    l3a1Table.append(out)

for i in range(100000, 5000000, 100000):
    trap = trapezeMethod.TrapezeMethod(0, 2*math.pi, i)
    out = abs(7.6404 - trap.calculateIntegral(sinFunc2))
    l3a2Table.append(out)

for i in range(100000, 5000000, 100000):
    simp = simpsonMethod.SimpsonMethod(0, 2*math.pi, i)
    out = abs(7.6404 - simp.calculateIntegral(sinFunc2))
    l3a3Table.append(out)

print(sum(l3a1Table))
print('==================')
print(sum(l3a2Table))
print('==================')
print(sum(l3a3Table))


a1 = s1a1Table + s2a1Table + s3a1Table + s4a1Table + l1a1Table + l2a1Table + l3a1Table
a2 = s1a2Table + s2a2Table + s3a2Table + s4a2Table + l1a2Table + l2a2Table + l3a2Table
a3 = s1a3Table + s2a3Table + s3a3Table + s4a3Table + l1a3Table + l2a3Table + l3a3Table

print(sum(a1))
print('==================')
print(sum(a2))
print('==================')
print(sum(a3))