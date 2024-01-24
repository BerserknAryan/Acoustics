import math
from formulas import conversion
from Area import area_formulas


def define_shape(shape, dimensions):
    if shape in area_formulas:
        dimensions = [float(dim) for dim in dimensions.split(',')]
        return area_formulas(shape, dimensions)
    else:
        return "Invalid shape"


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
    print("1. Tubular")
    print("2. Cuboid")
    print("3. Wedge")
    print("4. Wedge2")
    print("5. "Polygon")
    print("6. Elliptical")
    print("7. Conical")

    # Get user input for shape selection
    selected_shape_num = int(input("Enter the number of the shape: "))

    # Mapping numbers to shapes
    shape_mapping = {
        1: 'circle',
        2: 'rectangle',
        3: 'wedge',
        4: 'wedge2',
        5: 'polygon'
        6: 'elliptical',
        7: 'conical'
    }

    selected_shape = shape_mapping.get(selected_shape_num)

    generate_panel_dimensions(selected_shape)


def generate_panel_dimensions(selected_shape):
    if selected_shape:
        # Get user input for dimensions
        dimensions_input = input("Enter the dimensions (comma-separated): ")
        shape_math = define_shape(selected_shape, dimensions_input)

        # Display the result
        print(f"The volume of the {selected_shape} is: {shape_math}")
    else:
        print("Invalid shape number. Please enter a valid number.")

    # Get user inputs
    num_drivers = int(input("Enter the number of drivers: "))
    vas = float(input("Enter the Vas (equivalent air volume) of the driver: "))
    qts = float(input("Enter the Qts (total Q factor) of the driver: "))
    max_dimensions = [float(input("Enter the maximum length: ")),
                      float(input("Enter the maximum width: ")),
                      float(input("Enter the maximum height: "))]
    desired_qtc = float(input("Enter the desired QTC (Total Q factor for sealed enclosure): "))

    # Replace the previous enclosure calculation with the new enclosures library
    enclosure_type = 'sealed'  # Adjust as needed based on your application
    parameters_enclosure = [desired_qtc, vas, resonance_frequency]  # Adjust as needed based on your application

    result_enclosure = enclosures(enclosure_type, parameters_enclosure)

    # Display the results
    print("\nEnclosure Results:")
    for parameter, value in result_enclosure.items():
        print(f"{parameter}: {value}")

    # Display the results
    print(f"\nRecommended Volume: {recommended_volume} cubic units")
    print(f"Resonance Frequency: {resonance_frequency} Hz")
    print(f"F3 (Cutoff Frequency): {f3} Hz")

    # Generate panel dimensions based on the selected shape
    if selected_shape in ['circle', 'rectangle']:
        length = math.pow(recommended_volume, 1/3)
        width = length
        height = length
    elif selected_shape == 'wedge':
        # Adjust dimensions based on the specific shape requirements
        length = math.pow(recommended_volume, 1/3)
        width = length
        height = length
    elif selected_shape == 'wedge2':
        # Adjust dimensions based on the specific shape requirements
        length = math.pow(recommended_volume, 1/3)
        width = length
        height = length

    print("\nGenerated Panel Dimensions:")
    print(f"Length: {length} units")
    print(f"Width: {width} units")
    print(f"Height: {height} units")


def main():
    get_system()


if __name__ == "__main__":
    main()
