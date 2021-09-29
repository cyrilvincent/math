import scipy.integrate as integrate
import numpy as np

result = integrate.quad(np.sin, -np.inf, +np.inf)
print(result)
