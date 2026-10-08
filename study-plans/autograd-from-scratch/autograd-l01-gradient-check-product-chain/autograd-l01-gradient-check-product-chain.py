import numpy as np

def calc_e(a,b,c):
    e = float(a)*float(b) + float(c)
    return e

def gradient_check_product_chain(
    a: float,
    b: float,
    c: float,
    f: float,
    h: float,
) -> tuple[float, list, list, float]:
    """
    Returns loss, analytic gradients, numerical gradients, and maximum error.
    """
    e = calc_e(a,b,c)
    N_f = (e*(f+h) - e*f)/h
    N_a = (calc_e(a+h, b, c)*f - calc_e(a,b,c)*f)/h
    N_b = (calc_e(a, b+h, c)*f - calc_e(a,b,c)*f)/h
    N_c = (calc_e(a, b, c+h)*f - calc_e(a,b,c)*f)/h
    L = calc_e(a,b,c)*f
    A_f = calc_e(a,b,c)
    A_a = f*b
    A_b = f*a
    A_c = f
    ans_a = L
    ans_b = [float(A_a), float(A_b),float(A_c), float(A_f)]
    ans_c = [float(N_a), float(N_b),float(N_c), float(N_f)]
    diff_max = max([abs(ans_b[i]-ans_c[i]) for i in range(4)])
    return ans_a, ans_b, ans_c, diff_max
