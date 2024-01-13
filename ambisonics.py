import numpy as np
import scipy.special

class Ambisonics:
    @staticmethod
    def acn(order=1):
        for n in range(order + 1):
            for m in range(-n, n + 1):
                yield (n, m)

    @staticmethod
    def sn3d(m, n):
        m = np.atleast_1d(m)
        n = np.atleast_1d(n)

        d = np.logical_not(m.astype(bool))
        out = np.sqrt((2.0 - d) / (4.0 * np.pi) * scipy.special.factorial(n - np.abs(m)) / scipy.special.factorial.factorial(n + np.abs(m)))
        return out

    @staticmethod
    def n3d(m, n):
        n = np.atleast_1d(n)
        return Ambisonics.sn3d(m, n) * np
