#    DoubleUnaryOperator circleFunction = x -> Math.sqrt(1 - x * x);
#     DoubleUnaryOperator circleDerivative = x -> -x / Math.sqrt(1 - x * x);
import math
from algorythms import ractangleMethod

circleFunction = lambda x : math.sqrt(1 - x * x)
   
rec = ractangleMethod.RactangleMethod(-1, 1, 100000)

print(rec.calculateIntegral(circleFunction)*2) # *2 bo to połowa koła
print(math.pi)

# S1 pola koła o promieniu 1 (i wyznaczenie z niego przybliżenia wartości liczby π), π