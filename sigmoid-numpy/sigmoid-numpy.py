import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    vec = np.asarray(x, dtype=float)
    
    return 1 / (1 + np.exp(-vec))