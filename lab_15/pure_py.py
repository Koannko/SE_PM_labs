def f(i):
    return (5 * i**2 - 8) / (i**3 + 1)

def g(j):
    return (j + 1)**0.5 - j**0.5 - 0.5

def calc_matrix(n, m):
    max_a = 0
    for i in range(1, n+1):
        for j in range(1, m+1):
            a = abs(f(i) + g(j))
            if a > max_a:
                max_a = a
    return (n * m)**0.5 * max_a

if __name__ == '__main__':
    print(calc_matrix(10, 10))

# Обычный запуск
# $executionTime = Measure-Command { python pure_py.py }
# $executionTime.TotalSeconds
# >> 0.0780925

# Запуск с помощью PyPy
# $executionTime = Measure-Command { python pure_py.py }
# $executionTime.TotalSeconds
# >> 0.0674667