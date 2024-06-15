# Done
import numpy as np
import matplotlib.pyplot as plt
from Equation import Expression


def equation(equation,variables):
    f = Expression(equation,variables)
    return f

class Trapezium_integration:

    def function_integration(self, a, b, N):
        h = (b - a) / N
        summation = 0.5*(f(a) + f(b))
        for i in range(1, N):
            summation += f(a + i * h)
        summation *= h
        return summation
        
    
    def data_integration(self, data):   
        N = len(data)
        h = (data[-1] - data[0]) / N
        summation = 0.5*(data[0] + data[-1])
        for i in range(N):
            summation += (data[i])
        summation *= h
        return summation 

class simpson:

    def one_third(self,a,b,N):
        h = (b - a) / N
        summation = (f(a) + f(b))
        term = 0
        for i in range(1, N, 2):
            term += 4*f(a + i * h)
        for i in range(2,N,2):
            term += 2*f(a + i * h)
        summation = (summation+term)*h/3
        return summation
    def three_eight(self,a,b,N):
        h = (b - a) / N
        summation = (f(a) + f(b))
        term = 0
        for i in range(1,N):
            if i%3==0:
                term += 2*f(a+i*h)
            else:
                term += 3*f(a+i*h)
        summation = (summation + term ) * h *3 / 8
        return summation




def f(x):
    return 3*x**2       

while (1):
    print("1.Trapezium Rule Integration ")
    print("2. Trapezium Rule data Integration")
    print("3. simpson 1/3 integration ")
    print("4. simpson 3/8 integration")

    ask = input("<")
    if (ask == "1"):
        print("integration using trapezium function integration is ")
        a = float(input("lower limit a= "))
        b = float(input("upper limit b= "))
        N = int(input("number of steps N= "))
        test1 = Trapezium_integration().function_integration(a,b,N)
        print(test1)
    elif (ask == "2"):
        print("integrating using trapezium data integration ")
        data = np.loadtxt(r"C:\Users\SANDEEP\Desktop\python practice\desktop files\swim_vol.txt",float)
        
        test2 = Trapezium_integration().data_integration(data)
        print(test2)
    elif (ask == "3"):
        print("integrating using simpson rule ")
        a = float(input("lower limit a= "))
        b = float(input("upper limit b= "))
        N = int(input("number of steps N= "))
        
        test3 = simpson().one_third(a,b,N)
        print(test3)
    elif (ask == "4"):
        print("integrating using simpson rule ")
        a = float(input("lower limit a= "))
        b = float(input("upper limit b= "))
        N = int(input("number of steps N= "))
        test4 = simpson().three_eight(a,b,N)
        print(test4)
    elif (ask == "5"):
        break
    else:
        print("not a valid option")
