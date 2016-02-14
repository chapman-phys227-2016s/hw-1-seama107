#!/usr/bin/python
import math

def trapezint(f, a, b, n) :
    """
    Just for testing - uses trapazoidal approximation from on f from a to b with
    n trapazoids
    """
    output = 0.0
    for i in range(int(n)):
        f_output_lower = f( a + i * (b - a) / n )
        f_output_upper = f( a + (i + 1) * (b - a) / n )
        output += (f_output_lower + f_output_upper) * ((b-a)/n) / 2 
    return output

def second_derivative_approximation(f, x, h = .001):
    """
    Approximates the second derivative with h (dx) = .001
    """
    return (f(x + h) - 2 * f(x) + f(x - h))/h**2


def adaptive_trapezint(f, a, b, eps=1E-5):
    """
    Uses trapazoidal approximation on f from a to b with an error value
    of less than epsilon, to calculate the number of trapazoids
    """
    max_second_derivative = 0
    for i in range(10000):
        i_second_d = abs(second_derivative_approximation(f, a + i * (b - a)/10000))
        if( i_second_d > max_second_derivative):
            max_second_derivative = i_second_d
    h = math.sqrt(12 * eps / ((b - a) * max_second_derivative))
    #There is a clear problem here, as if the second derivative is zero, 
    #h will become too large and there will be no approximation
    n = (b - a)/h
    return trapezint(f, a, b, n)




