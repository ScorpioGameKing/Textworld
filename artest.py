import opensimplex as opsm
import numpy as np

opsm.random_seed()

width = 10
height = 10

_w = np.array([x for x in range(10)])
_h = np.array([x for x in range(10)])
_z = np.array([1])

noise = opsm.noise2array(_w, _h)

print(noise)