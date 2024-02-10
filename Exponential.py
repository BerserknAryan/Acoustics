import math


# this file will contain the formulas for the exponential horn.
# Basshorn.py will call these formulas to calculate the horn dimensions and response.
# at = throat area, amt = mouth area, ax = cross-sectional area, L = horn length,
class Exponential
    @staticmethod
    def calculate_exp_rate_of_flare(at, amt, length):
        return amt / (1 + (2 / (math.exp((2 * length) / (at * amt))) - 1))

    @staticmethod
    def calculate_exp_rate_of_flare_constant(rate_of_flare, at, ax):
        return (2 * math.atan(rate_of_flare * ax / (2 * at)) - 2 * math.atan
                (rate_of_flare * 0 / (2 * at)))
