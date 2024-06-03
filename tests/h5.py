import math
import matplotlib.pyplot as plt
import sys
sys.path.append("..")
from algorythms import simpsonMethod

def rotate_vector(vector, alpha):
    x, y = vector
    new_x = x * math.cos(alpha) - y * math.sin(alpha)
    new_y = x * math.sin(alpha) + y * math.cos(alpha)
    return (new_x, new_y)

def count_circumference(n, alpha, vector):
    init = (1, 0)
    current = init
    circumference = 0
    for _ in range(n):
        prev = current
        current = (current[0] + vector[0], current[1] + vector[1])
        circumference += math.sqrt((current[0] - prev[0])**2 + (current[1] - prev[1])**2)
        vector = rotate_vector(vector, alpha)
    return circumference

circleFunction = lambda x : math.sqrt(1 - x * x)

if __name__ == "__main__":
    distances = []
    simpTable = []
    for i in range(1000000, 10000001, 1000000):
        alpha = 2 * math.pi / i
        vector = (math.cos(alpha) - 1, math.sin(alpha))
        temp = abs(math.pi - count_circumference(i, alpha, vector)/2)
        distances.append(temp)

        simp = simpsonMethod.SimpsonMethod(-1, 1, i)
        res = abs(math.pi - simp.calculateIntegral(circleFunction) * 2)
        simpTable.append(res)
        print(i)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(range(1000000, 10000001, 1000000), distances, s=5, c='blue', alpha=0.5)
    plt.scatter(range(1000000, 10000001, 1000000), simpTable, s=5, c='green', alpha=0.5)
    plt.yscale('log')
    plt.grid(True)
    plt.show()
