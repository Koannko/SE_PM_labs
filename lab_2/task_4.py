# Найти все числа Армстронга из 2, 3 и 4 цифр. Число Армстронга — такое число из
# k цифр, что сумма
# k-х степеней его цифр равна самому числу

is_arm_num = 0

for k in range(10, 100):
    is_arm_num = (int(k / 10))**2 + (k % 10)**2
    if (k == is_arm_num):
        print(is_arm_num)

for k in range(100, 1000):
    is_arm_num = (int(k / 100))**3 + (int(k % 100 / 10))**3 + (k % 10)**3
    if (k == is_arm_num):
        print(is_arm_num)

for k in range(1000, 10000):
    is_arm_num = (int(k / 1000))**4 + (int(k % 1000 / 100))**4 + \
        (int(k % 100 / 10))**4 + (k % 10)**4
    if (k == is_arm_num):
        print(is_arm_num)
