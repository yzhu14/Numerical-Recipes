import numpy as np

"""---------Functions--------"""


def polynomial(x):
	return x**3 - 2.1*x**2 - 7.4*x + 10.2
def exponential(x):
    return np.exp(x)-2

"""Derivatives"""
def poly_prime(x):
    return 3*x**2 - 4.2*x - 7.4
def exp_prime(x):
    return np.exp(x)

true_root_poly_a, true_root_poly_b, true_root_poly_c = -2.49771, 1.20296, 3.39475
true_root_exp = 0.693147



