def expression(a, b, c):
    d = a*b + c
    return d

def scalar_expression_partials(a: float, b: float, c: float, h: float) -> tuple[float, float, float, float]:
    """
    Returns the expression value and numerical partials for a, b, and c.
    """
    d = expression(a, b, c)
    d_a = (expression(a+h, b, c) - d)/h
    d_b = (expression(a, b+h, c) - d)/h
    d_c = (expression(a, b, c+h) - d)/h
    return float(d), float(d_a), float(d_b), float(d_c)
