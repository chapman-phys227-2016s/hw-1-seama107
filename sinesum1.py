#!/usr/bin/python
import math

def f(t, T):
    """
    returns -1, 0, or 1 based on relationship between t and T
    throws IndexError
    """
    if(t > 0 and t < float(T/2)):
        return 1
    elif(t == float(T/2)):
        return 0
    elif(t > float(T/2) and t < T):
        return -1

    raise IndexError("Out of function domain")

def S(t, n, T):
    """
    Sinosoidal approximation of f with n as the number of approximations
    """
   
    output = 0.0
    for i in range(n):
        output += math.sin(2 * math.pi * t * (2*i + 1) / T) / (2*i + 1)
    return (4/math.pi) * output

def test_f():
    assert(f(0,0) == 0)
    assert(f(.5,2) == 1)
    assert(f(1.5,2) == -1)
    
def calc_error(n,a,T):
    apr = S(a*T, n, T)
    exact = f(a*T,T)
    return exact - apr

def print_error_results(list_of_n = [1,3,5,10,30,100], list_of_alpha = [.01,.25,.49]):
    print "alphas:",
    for a in list_of_alpha:
        print "   {0:.3g}".format(a),
    print
    for n in list_of_n:
        print "n: {0}  ".format(n),
        for a in list_of_alpha:
            print "   {0:+.3g}".format(calc_error(n,a,2*math.pi)),
        print



