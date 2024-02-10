import math


#Basshorn.py will use Hyperbolic to calculate the rate of flare for a horn
# at, amt, and length are the throat area, mouth area, and length of the horn, respectively
#ax is the cross-sectional area of the horn
class Hyperbolic:
    @staticmethod
    def calculate_hyp_rate_of_flare(at, amt, length):
        return (math.pi * at ** 2) / (1 + (2 / (math.exp((2 * length) / (at * amt))) - 1))

    @staticmethod
    def calculate_hyp_rate_of_flare_constant(rate_of_flare, at, ax):
        return (2 * math.atan(rate_of_flare * ax / (2 * at)) - 2 * math.atan
                (rate_of_flare * 0 / (2 * at)))