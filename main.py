import math
from algorythms import ractangleMethod
from algorythms import trapezeMethod
from algorythms import simpsonMethod

circleFunction = lambda x : math.sqrt(1 - x * x)
uFunc = lambda x : x * x
   
rec = ractangleMethod.RactangleMethod(-1, 1, 100000)
trap = trapezeMethod.TrapezeMethod(-1, 1, 100000)
simp = simpsonMethod.SimpsonMethod(-1, 1, 100000)

print(rec.calculateIntegral(uFunc) *2) # *2 bo to połowa koła
print(trap.calculateIntegral(uFunc) *2)
print(simp.calculateIntegral(uFunc) *2)
print(math.pi)

3.1415925484068286
3.1415925484068286
3.1415926125132096
3.141592653589793