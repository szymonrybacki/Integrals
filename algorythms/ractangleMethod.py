class RactangleMethod:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n
    
    def calculateIntegral(self, func):
        sum = 0.0
        dx = (self.b - self.a) / self.n
        
        for i in range (0, self.n):
            x = self.a + i * dx
            sum += func(x) * dx
        
        return sum
