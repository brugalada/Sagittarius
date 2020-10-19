"""
Empirical interpolators for the Sagittarius stream: distance and proper motions
"""

__version__ = "0.0.1"

try:
    import numpy
except ImportError:
    raise ImportError('NumPy does not seem to be installed.')

try:
    import scipy
except ImportError:
    raise ImportError('Scipy does not seem to be installed.')

import sagittarius.sagittarius_properties