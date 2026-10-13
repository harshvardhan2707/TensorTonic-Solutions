import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    x1 = np.asarray(x)
    x2 = np.asarray(p)
    return float(np.dot(x1,x2))