#!/usr/bin/python
import math

def diff(f, x, h=1E-5):
    """
    Gives the derivative on f at point x aproximated by
    the average change in the function over the interval 2h
    """
    return (f(x + h) - f(x - h))/(2*h)

def some_function(x):
    return x**2 + 6*x

def test_diff():
    assert(diff(some_function,4) == 14)
    
def f1(x):
    return math.pow(math.e, x)

def f2(x):
    return math.pow(math.e, -2*x**2)

def f3(x):
    return math.cos(x)

def f4(x):
    return math.log(x)


def application(list_of_functions = [f1, f2, f3, f4], list_of_x = [0,0,math.pi * 2, 1], list_of_answers = [1,0,0,1]):
    """
    Calculates the "diff" of each function at x and finds the difference
    between that and the mathmatical answer
    """
    for fi, xi, ai in zip(list_of_functions, list_of_x, list_of_answers):
        diff_result = diff(fi, xi, h=.01)
        error = ai - diff_result
        print "Result: {1}, answer: {2}, difference {3}".format(fi, diff_result, ai, error)


