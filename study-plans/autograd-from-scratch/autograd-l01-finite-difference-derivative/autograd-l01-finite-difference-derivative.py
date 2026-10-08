import numpy as np

def finite_difference_derivative(coefficients: list, x: float, h: float) -> tuple[float, float, float]:
    """
    Returns the value at x, the value at x plus h, and the estimated slope.
    """
    n = len(coefficients)
    f_x = [coefficients[i]*(x**i) for i in range(n)]
    f_x_h = [coefficients[i]*((x+h)**i) for i in range(n)]
    return float(sum(f_x)), float(sum(f_x_h)), float((sum(f_x_h) - sum(f_x))/h)
