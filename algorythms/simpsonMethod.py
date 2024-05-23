class SimpsonMethod:
    def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n

    def calculateIntegral(self, fun):
        dx = (self.b - self.a) / self.n

        sum1 = 0.0
        for i in range(1, self.n, 2):
            sum1 += 4*fun(self.a + i * dx)

        sum2 = 0.0
        for i in range(2, self.n-1, 2):
            sum2 += 2*fun(self.a + i * dx)

        integral = (dx/3)*(fun(self.a) + fun(self.b) + sum1 + sum2)
        return integral