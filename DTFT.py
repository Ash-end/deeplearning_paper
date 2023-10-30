
import matplotlib.pyplot as plt
import numpy as np

# Define two discrete time sequences
sequence1 = [1, 2, 3, 4, 5]
sequence2 = [5, 4, 3, 2, 1]

# Sum operation
sum_result = [x + y for x, y in zip(sequence1, sequence2)]

# Plot the result of the sum operation
plt.subplot(221)
plt.stem(range(len(sum_result)), sum_result)
plt.title('Sum Operation')

# Product operation
product_result = [x * y for x, y in zip(sequence1, sequence2)]

# Plot the result of the product operation
plt.subplot(222)
plt.stem(range(len(product_result)), product_result)
plt.title('Product Operation')

# Shift operation
shift_amount = 2  # Shift to the right by 2 positions
shifted_result = [0] * shift_amount + sequence1[:-shift_amount]

# Plot the result of the shift operation
plt.subplot(223)
plt.stem(range(len(shifted_result)), shifted_result)
plt.title('Shift Operation')

# Flip operation
flipped_result = [x for x in reversed(sequence1)]

# Plot the result of the flip operation
plt.subplot(224)
plt.stem(range(len(flipped_result)), flipped_result)
plt.title('Flip Operation')

plt.tight_layout()
plt.show()
