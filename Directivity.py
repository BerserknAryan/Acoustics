# directivity

import math


class Directivity:
    
    @staticmethod
    def dbsum(levels, axis=None):
        # Energetic summation of levels. Formula:
        # L_{sum} = 10 \\ log_{10}{\\sum_{i=0}^n{10^{L/10}}}
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0)).sum(axis=axis))

    @staticmethod
    def dbmean(levels, axis=None):
        # Energetic average of levels. Formula:
        # L_{mean} = 10 \\ log_{10}{\\frac{1}{n}\\sum_{i=0}^n{10^{L/10}}}
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0)).mean(axis=axis))

    @staticmethod
    def dbadd(a, b):
        # Energetic addition. Formula:
        # L_{a+b} = 10 \\ log_{10}{10^{L_b/10}+10^{L_a/10}} #
        a = np.asanyarray(a)
        b = np.asanyarray(b)
        return 10.0 * np.log10(10.0 ** (a / 10.0) + 10.0 ** (b / 10.0))

    @staticmethod
    def dbsub(a, b):
        # Energetic subtraction. Formula:
        # L_{a-b} = 10 \\ log_{10}{10^{L_a/10}-10^{L_b/10}} #
        a = np.asanyarray(a)
        b = np.asanyarray(b)
        return 10.0 * np.log10(10.0 ** (a / 10.0) - 10.0 ** (b / 10.0))

    @staticmethod
    def dbmul(levels, f, axis=None):
        # Energetically add `levels` `f` times. Formula:
        # L_{sum} = 10 \\ log_{10}{\sum_{i=0}^n{10^{L/10} \cdot f}} #
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0) * f).sum(axis=axis))

    @staticmethod
    def dbdiv(levels, f, axis=None):
        # Energetically divide `levels` `f` times. Formula:
        # L_{sum} = 10 \\ log_{10}{\\sum_{i=0}^n{10^{L/10} / f}} #
        levels = np.asanyarray(levels)
        return 10.0 * np.log10((10.0 ** (levels / 10.0) / f).sum(axis=axis))


__all__ = ['dbsum', 'dbmean', 'dbadd', 'dbsub', 'dbmul', 'dbdiv']
