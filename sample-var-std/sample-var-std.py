import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    # Write code here
    a = np.asarray(x)
    mean = np.mean(x)
    a = np.sum(np.square(a-mean))
    var = a/(len(x)-1)
    return {"variance": float(var), "standard_deviation": float(np.sqrt(var))}
    