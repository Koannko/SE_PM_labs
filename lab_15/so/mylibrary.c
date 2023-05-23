#include <math.h>

double f(int i) {
    return (5 * pow(i, 2) - 8) / (pow(i, 3) + 1);
}

double g(int j) {
    return sqrt(j + 1) - sqrt(j) - 0.5;
}

double calc_matrix(int n, int m) {
    double max_a = 0;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            double a = fabs(f(i) + g(j));
            if (a > max_a) {
                max_a = a;
            }
        }
    }
    return sqrt(n * m) * max_a;
}

// gcc -shared -o mylibrary.dll mylibrary.c