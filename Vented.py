import math


class Vented:
    def __init__(self, vas, fs, qts, vb):
        self.vas = vas
        self.fs = fs
        self.qts = qts
        self.vb = vb

    @staticmethod
    def theoretical_cut_off_frequency(self):
        # Formula for calculating the theoretical cut-off frequency
        return 0.26 * self.fs * (self.qts ** -1.4)

    @staticmethod
    def tuning_frequency(self):
        # Formula for calculating the tuning frequency
        return 0.42 * self.fs * (self.qts ** -0.9)

    @staticmethod
    def f3(self, vb):
        # Formula for finding F3
        return ((self.vas / vb) ** 0.5) * self.fs

    @staticmethod
    def new_tuning_frequency(self, vb):
        # Formula for calculating the new tuning frequency
        return ((self.vas / vb) ** 0.32) * self.fs

    @staticmethod
    def port_diameter_for_driver(self):
        # Determine port diameter for drivers in vented and bandpass boxes
        if 6 <= self.driver_diameter <= 8:
            return 3
        elif 8 < self.driver_diameter <= 10:
            return 4
        elif 10 < self.driver_diameter <= 12:
            return 5
        elif 12 < self.driver_diameter <= 15:
            return 6
        elif 15 < self.driver_diameter <= 18:
            return 8
        elif 18 < self.driver_diameter <= 21:
            return 10
        elif 21 < self.driver_diameter <= 26:
            return 16
        elif 26 < self.driver_diameter <= 32:
            return 22

    @staticmethod
    def port_length(vb, fb, port_diameter):
        # Formula for calculating the port length
        port_radius = port_diameter / 2
        vb_cubic_inches = vb * 1728
        return (1.463 * (10 ** 7) * (port_radius ** 2) / (fb ** 2) * vb_cubic_inches) - 1.463 * port_radius

    @staticmethod
    def equivalent_port_diameter(ports_diameters):
        # Calculate equivalent cross-sectional area of multiple ports that will equal a single, larger port
        sum_of_squares = sum(d ** 2 for d in ports_diameters)
        return sum_of_squares ** 0.5