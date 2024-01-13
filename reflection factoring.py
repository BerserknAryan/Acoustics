import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc


# can add reflections into your enclosure calculations or plot the reflection factoring

class BoundaryCalculator:
    SPECIFIC_HEAT_RATIO = 1.4
    POROSITY_DECREASE = 120.0
    SOUNDSPEED = 343.0
    DENSITY = 1.296

    def __init__(
            self,
            frequency,
            flow_resistivity,
            density=DENSITY,
            soundspeed=SOUNDSPEED,
            porosity_decrease=POROSITY_DECREASE,
            specific_heat_ratio=SPECIFIC_HEAT_RATIO,
            angle=None,
            distance=None,
            impedance_model='db',
            reflection_model='plane',
    ):
        self.frequency = frequency
        self.flow_resistivity = flow_resistivity
        self.density = density
        self.soundspeed = soundspeed
        self.porosity_decrease = porosity_decrease
        self.specific_heat_ratio = specific_heat_ratio
        self.angle = angle
        self.distance = distance
        self.impedance_model = impedance_model
        self.reflection_model = reflection_model

    @property
    def wavenumber(self):
        return 2.0 * np.pi * self.frequency / self.soundspeed

    @property
    def impedance(self):
        if self.impedance_model == 'db':
            return impedance_delany_and_bazley(self.frequency, self.flow_resistivity)
        elif self.impedance_model == 'att':
            return impedance_attenborough(
                self.frequency,
                self.flow_resistivity,
                self.density,
                self.soundspeed,
                self.porosity_decrease,
                self.specific_heat_ratio,
            )
        else:
            raise ValueError("Incorrect impedance model.")

    @property
    def reflection_factor(self):
        if self.angle is None:
            raise AttributeError('Cannot calculate reflection factor. self.angle has not been specified.')

        if self.reflection_model == 'plane':
            return reflection_factor_plane_wave(*np.meshgrid(self.impedance, self.angle))
        elif self.reflection_model == 'spherical':
            if self.distance is None:
                raise AttributeError('Cannot calculate reflection factor. self.distance has not been specified.')
            else:
                return reflection_factor_spherical_wave(
                    *np.meshgrid(self.impedance, self.angle),
                    distance=self.distance,
                    wavenumber=self.wavenumber,
                )
        else:
            raise RuntimeError("Oops...")

    def plot_impedance(self, filename=None):
        fig = plt.figure()

        ax0 = fig.add_subplot(211)
        ax0.set_title('Magnitude of impedance')
        ax0.semilogx(self.frequency, np.abs(self.impedance))
        ax0.set_xlabel(r'$f$ in Hz')
        ax0.set_ylabel(r'$\left|Z\right|$')
        ax0.grid()

        ax0 = fig.add_subplot(212)
        ax0.set_title('Angle of impedance')
        ax0.semilogx(self.frequency, np.angle(self.impedance))
        ax0.set_xlabel(r'$f$ in Hz')
        ax0.set_ylabel(r'$\angle Z$')
        ax0.grid()

        plt.tight_layout()

        if filename:
            fig.savefig(filename, transparent=True)
        return fig

    def plot_reflection_factor(self, filename=None):
        if self.frequency is None:
            raise ValueError("No frequency specified.")
        if self.angle is None:
            raise ValueError("No angle specified.")

        try:
            n_f = len(self.frequency)
        except TypeError:
            n_f = 1
        try:
            n_a = len(self.angle)
        except TypeError:
            n_a = 1

        if n_f == 1 and n_a == 1:
            raise ValueError("Either frequency or angle needs to be a vector.")

        elif n_f == 1 or n_a == 1:
            if n_f == 1 and n_a > 1:
                xlabel = r"$\theta$ in degrees"
            elif n_f > 1 and n_a == 1:
                xlabel = r"$f$ in Hz"
            R = self.reflection_factor
            fig = plt.figure()

            ax0 = fig.add_subplot(211)
            ax0.set_title("Magnitude of reflection factor")
            ax0.semilogx(self.frequency, np.abs(R))
            ax0.set_xlabel(xlabel)
            ax0.set_ylabel(r'$\left|R\right|$')
            ax0.grid()

            ax1 = fig.add_subplot(212)
            ax1.set_title("Phase of reflection factor")
            ax1.semilogx(self.frequency, np.angle(R))
            ax1.set_xlabel(xlabel)
            ax1.set_ylabel(r'$\angle R$')
            ax1.grid()

        elif n_f > 1 and n_a > 1:
            R = self.reflection_factor
            fig = plt.figure()

            ax0 = fig.add_subplot(211)
            ax0.set_title("Magnitude of reflection factor")
            ax0.pcolormesh(self.frequency, self.angle * 180.0 / np.pi, np.abs(R))
            ax0.grid()

            ax1 = fig.add_subplot(212)
            ax1.set_title("Phase of reflection factor")
            ax1.pcolormesh(self.frequency, self.angle * 180.0 / np.pi, np.angle(R))
            ax1.grid()

        else:
            raise RuntimeError("Oops...")

        if filename:
            fig.savefig(filename, transparent=True)
        else:
            return fig


class ReflectionFactorPlotter:
    @staticmethod
    def plot_impedance_and_reflection(boundary_calculator, impedance_filename=None, reflection_filename=None):
        impedance_plot = boundary_calculator.plot_impedance(filename=impedance_filename)
        reflection_plot = boundary_calculator.plot_reflection_factor(filename=reflection_filename)
        return impedance_plot, reflection_plot


def reflection_factor_plane_wave(impedance, angle):
    return (impedance * np.cos(angle) - 1.0) / (impedance * np.cos(angle) + 1.0)


def numerical_distance(impedance, angle, distance, wavenumber):
    return np.sqrt(-1j * wavenumber * distance *
                   (1.0 + 1.0 / impedance * np.cos(angle) - np.sqrt(1.0 - (1.0 / impedance)**2.0) * np.sin(angle)))


def reflection_factor_spherical_wave(impedance, angle, distance, wavenumber):
    w = numerical_distance(impedance, angle, distance, wavenumber)
    F = 1.0 - 1j * np.sqrt(np.pi) * w * np.exp(-w**2.0) * erfc(1j * w)

    plane_factor = reflection_factor_plane_wave(impedance, angle)
    return plane_factor * (1.0 - plane_factor) * F


def impedance_delany_and_bazley(frequency, flow_resistivity):
    return 1.0 + 9.08 * (1000.0 * frequency / flow_resistivity)**(-0.75) - 1j * 11.9 * (
        1000.0 * frequency / flow_resistivity)**(-0.73)


def impedance_attenborough(
        frequency,
        flow_resistivity,
        density=DENSITY,
        soundspeed=SOUNDSPEED,
        porosity_decrease=POROSITY_DECREASE,
        specific_heat_ratio=SPECIFIC_HEAT_RATIO,
):
    return (1.0 - 1j) * np.sqrt(flow_resistivity / frequency) / np.sqrt(
        np.pi * specific_heat_ratio * density) - 1j * soundspeed * porosity_decrease / (
            8.0 * np.pi * specific_heat_ratio * frequency)
