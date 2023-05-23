from ctypes import c_int, c_double, CDLL

if __name__ == '__main__':    
    my_functions = CDLL("D:\SE_PM_labs\lab_15\so\mylibrary.dll")
    my_functions.f.argtypes = [c_int]
    my_functions.f.restype = c_double
    my_functions.g.argtypes = [c_int]
    my_functions.g.restype = c_double
    my_functions.calc_matrix.argtypes = [c_int, c_int]
    my_functions.calc_matrix.restype = c_double
    
    result = my_functions.calc_matrix(10, 10)
    print(result)


# $executionTime = Measure-Command { python main.py }
# $executionTime.TotalSeconds
# 0.0832677