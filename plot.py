"""
Generate Cumulative Distribution Function of matrix A using matplotlib and numpy
"""
import numpy as np
import matplotlib.pyplot as plt

a = np.load("a.npy")

count, bins_count = np.histogram(a, 2000)

# Calculate CDF using probability distribution function (PDF)
pdf = count / sum(count)
cdf = np.cumsum(pdf)

plt.plot(bins_count[1:], cdf, label="CDF of A")
plt.title("Cumulative Distribute Function of values in random matrix A")
plt.legend()

plt.savefig("plot.png")
