import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfc
from IB import boundary_type

class Speaker_Location:
    def __init__(self, total_cms, effective_piston_area, cone_area, fs):
        # Initialize the <link>FreeAir</link> class with relevant parameters
        super().__init__(Speaker_Location="boundary_type")
        self.total_cms = total_cms
        self.effective_piston_area = effective_piston_area
        self.cone_area = cone_area
        self.fs = fs

    @staticmethod
    def trunk_resonant_frequency(total_cms, effective_piston_area, trunk_volume, fs):
        # Formula to calculate the resonant frequency for a speaker in the trunk
        return (1 / (2 * 3.141592) * np.sqrt
                (((total_cms + (trunk_volume * 1000)) /
                 effective_piston_area) + fs ** 2))

    @staticmethod
    def rear_deck_resonant_frequency(total_cms, effective_piston_area, fs):
        # Formula to calculate the resonant frequency for a speaker in the rear deck
        return (1 / (2 * 3.141592) * math.sqrt
                ((total_cms / effective_piston_area) + fs ** 2))

    @staticmethod
    def small_deck_resonant_frequency(total_cms, effective_piston_area, small_deck_volume, fs):
        # Formula to calculate the resonant frequency for a speaker mounted in or out of a small deck
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (small_deck_volume * 1000)) /
                    effective_piston_area) + fs ** 2))

    @staticmethod
    def floorboard_resonant_frequency(total_cms, effective_piston_area, cone_area, fs):
        # Formula to calculate the resonant frequency for a speaker installed in the
        # floorboard at the feet firing cone at you
        return 1 / (2 * 3.141592) * math.sqrt(((total_cms + (cone_area * 1000)) / 
                                               effective_piston_area) + fs ** 2)

    @staticmethod
    def trunk_resonant_frequency(total_cms, effective_piston_area, trunk_volume, fs):
        # Formula to calculate the resonant frequency for a speaker in the trunk
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (trunk_volume * 1000)) /
                 effective_piston_area) + fs ** 2))

    @staticmethod
    def cabin_resonant_frequency(total_cms, effective_piston_area, cabin_volume, fs):
        # Formula to calculate the resonant frequency for a speaker in the cabin
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (cabin_volume * 1000)) /
                  effective_piston_area) + fs ** 2))

    @staticmethod
    def ceiling_resonant_frequency(total_cms, effective_piston_area, ceiling_area, fs):
        # Formula to calculate the resonant frequency for a speaker in the ceiling
        return (1 / (2 * 3.141592) * math.sqrt
                (((total_cms + (ceiling_area * 1000)) /
                  effective_piston_area) + fs ** 2))

    def floorboard_resonant_frequency(self):
        # Formula to calculate the resonant frequency for a speaker installed in the floorboard
        return (1 / (2 * 3.141592) * np.sqrt
                (((self.total_cms + (self.cone_area * 1000)) /
                  self.effective_piston_area) + self.fs ** 2))
                  
                  
class InfiniteBaffleSpeaker:
    def __init__(self, total_cms, effective_piston_area, cone_area, fs, floorboard_volume):
        # Initialize the <link>InfiniteBaffleSpeaker</link> class with relevant parameters
        super().__init__(boundary_type="infinite baffle")
        self.total_cms = total_cms
        self.effective_piston_area = effective_piston_area
        self.cone_area = cone_area
        self.fs = fs
        self.floorboard_volume = floorboard_volume

    def plot_impedance(self):
        # Method to plot the impedance of the speaker based on its parameters
        # Implement the plotting logic for impedance
        pass

    def plot_impedance_and_reflection(self):
        self.plot_impedance()
        self.plot_reflection_factor()
        plt.show()

    def plot_reflection_factor(self):
        # Method to plot the reflection factor based on the boundary type
        frequency_range = np.linspace(10, 20000, 500)  # Adjust the frequency range as needed
        reflection_factor = self.calculate_reflection_factor(frequency_range)

        plt.plot(frequency_range, reflection_factor)
        plt.title('Reflection Factor for Infinite Baffle Speaker')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Reflection Factor')
        plt.grid(True)

    def calculate_reflection_factor(self, frequencies):
        # Function to calculate the reflection factor for each frequency
        reflection_factor = []
        for freq in frequencies:
            # Use the reflection factor formula for infinite baffle speakers
            # You may need to adjust this formula based on your specific requirements
            # For example, you can use the erfc function from scipy for more accurate calculations
            reflection_factor.append(0.5 * math.sin(math.radians(180 * (freq / self.fs))))

        return reflection_factor


# Example usage 1:
total_cms = 0.02
effective_piston_area = 0.07
cone_area = 0.03
fs = 90  # Resonant frequency of the speaker
floorboard_volume = 0.15  # Volume of the space behind the speaker in the floorboard
speaker = InfiniteBaffleSpeaker(total_cms, effective_piston_area, cone_area, fs, floorboard_volume)
resonant_frequency = speaker.floorboard_resonant_frequency()
print("Resonant Frequency for Floorboard Speaker:", resonant_frequency)

# Example usage 2:
speaker.plot_impedance_and_reflection()
