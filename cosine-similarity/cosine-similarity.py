import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    a = np.asarray(a)
    b = np.asarray(b)
    a_b = np.dot(a,b)
    a_l2 = np.sqrt(np.sum(a**2))
    b_l2 = np.sqrt(np.sum(b**2))
    if(a_b == 0):
        return float(0)
    return float(a_b/(a_l2*b_l2))