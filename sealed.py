import math
from formulas import area_formulas, enclosures, conversion


class Sealed:
    @staticmethod
    def optimal_sealed_volume(driver_vas, driver_qts, driver_fs):
        # Formula to calculate the optimal volume for a sealed enclosure
        return 0.9 * driver_vas / ((driver_qts ** 3) * (driver_fs ** 2))

    @staticmethod
    def air_spring_constant(enclosure_volume, driver_qts):
        # Formula to calculate the air spring constant for a sealed enclosure
        return (enclosure_volume * (driver_qts ** 2)) / 845

    @staticmethod
    def cutoff_frequency(enclosure_volume, driver_vas):
        # Formula to calculate the cutoff frequency for a sealed enclosure
        return (enclosure_volume / (driver_vas * 1.464)) ** 0.5

    @staticmethod
    def sealed_qtc(enclosure_volume, driver_vas):
        # Formula to calculate the enclosure Qtc for a sealed enclosure
        return (enclosure_volume / (driver_vas * 1.464)) ** 0.5

    @staticmethod
    def critical_damping_ratio(driver_qts):
        # Formula to calculate the critical damping ratio for a sealed enclosure
        return 0.707 / driver_qts


def get_system():
    # Select measurement system
    print("Select measurement system to use:")
    print("1. Metric (mm, cm^3)")
    print("2. Metric (cm, m^3)")
    print("3. Imperial (in, ft^3)")
    print("4. Imperial (ft, yd^3)")

    selected_system_num = int(input("Enter the number of the measurement system: "))

    # Mapping numbers to measurement systems
    system_mapping = {
        1: ('mm', 'cm^3'),
        2: ('cm', 'm^3'),
        3: ('in', 'ft^3'),
        4: ('ft', 'yd^3')
    }

    selected_system = system_mapping.get(selected_system_num)

    if selected_system:
        unit_length, _ = selected_system
    else:
        print("Invalid measurement system number. Please enter a valid number.")
        return

    # get enclosure shape
    print("List of shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Wedge")
    print("4. Wedge2")
    print("5. polygon")

    # Get user input for shape selection
    selected_shape_num = int(input("Enter the number of the shape: "))

    # Mapping numbers to shapes
    shape_mapping = {
        1: 'circle',
        2: 'rectangle',
        3: 'wedge',
        4: 'wedge2',
        5: 'polygon'
    }

    selected_shape = shape_mapping.get(selected_shape_num)



def main():
    get_system()


if __name__ == "__main__":
    main()
