digits = []
is_arm_num = 0
def armstrong_num():
    for k in range(10, 100):
        is_arm_num = (int(k / 10))**2 + (k % 10)**2
        if (k == is_arm_num):
            digits.append(is_arm_num)


    for k in range(100, 1000):
        if (k % 9 != 4 and k % 9 != 5):
            is_arm_num = (int(k / 100))**3 + (int(k % 100 / 10))**3 + (k % 10)**3
            if (k == is_arm_num):
                digits.append(is_arm_num)

    for k in range(1000, 10000):
        is_arm_num = (int(k / 1000))**4 + (int(k % 1000 / 100))**4 + (int(k % 100 / 10))**4 + (k % 10)**4
        if (k == is_arm_num):
            digits.append(is_arm_num)
    return digits
                                    
print(armstrong_num())