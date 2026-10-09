from collections import Counter
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    # Write code here
    sorted_x = sorted(x)
    n = len(x)
    mean = sum(x) / n
    median = (sorted_x[(n+1)//2 -1] + sorted_x[(n+1)//2 -1 + (n%2 + 1)%2])/2
    X = dict()
    for i in sorted_x:
        if i in X.keys():
            X[i]+=1
        else:
            X[i] = 1
    max_count = -1
    mode_value = 0
    for i, j in X.items():
        if(j>max_count):
            mode_value = i
            max_count = j
    return {"mean": float(mean), "median":float(median), "mode": float(mode_value)}