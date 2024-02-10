import math


class Conical:
    # amt = mouth area of the conical horn, at = throat area of the conical horn,
    # ax = cross-sectional area of the conical horn, length = length of the conical horn
    # rate_of_flare = rate of flare of the conical horn,
    # conical_rate_of_flare_constant = constant for conical rate of flare
    @staticmethod
    def calculate_con_rate_of_flare(at, amt, length):
        return (2 * math.pi * at * length) / (math.sqrt(1 + (at / length) ** 2))

    @staticmethod
    def calculate_con_rate_of_flare_constant(rate_of_flare, at, ax):
        return (2 * math.atan(rate_of_flare * ax / (2 * at)) - 2 * math.atan
                (rate_of_flare * 0 / (2 * at)))

# Basshorn.py will use the Conical class to calculate the rate of flare for a conical horn.# Enclosures.py will use the Conical class to calculate the rate of flare for a conical horn.