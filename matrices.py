"""
Generate random matrices and perform matrix multiplications on them.
"""

import numpy as np

def main():
    a = generate_random_matrix(size=(10**6,10**3), low=0.0, high=1.0)
    # save matrix into a binary file using numpy.save
    np.save("a", a)
    # Force freeing up memory by assinging the variable value None
    a = None

    b = generate_random_matrix(size=(10**3,10**6), low=0.0, high=1.0)
    np.save("b", b)

    c = generate_random_matrix(size=(10**6,1), low=0.0, high=1.0)
    np.save("c", c)

    # Multiply matrices using numpy.matmul
    bc = np.matmul(b,c)
    np.save("bc", bc)

    b,c = None,None

    a = np.load("a.npy")
    d = np.matmul(a, bc)

    np.save("d", d)
    a,d = None, None

def generate_random_matrix(size, high, low):
    """
    Generates a matrix with given size and a range of values using numpy random uniform.
    """
    return np.random.uniform(low=low, high=high, size=size)

if __name__ == "__main__":
    main()
