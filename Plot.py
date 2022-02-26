import matplotlib.pyplot as plt
import numpy as np

plt.title('Plot of f(x)')
plt.xlabel('x-label')
plt.ylabel('y-label')

x = np.arange(0, 3, 0.1)

plt.plot(x, (14*x*np.exp(x-2))-(12*np.exp(x-2))-(7*pow(x,3))+(20*pow(x,2))-(26*x)+12)

plt.show()
