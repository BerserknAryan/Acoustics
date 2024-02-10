import os
import json
import psutil


def list_available_drives():
    drives = [drive.device for drive in psutil.disk_partitions()]
    print("Available Drives:")
    for idx, drive in enumerate(drives, start=1):
        print(f"{idx}. {drive}")
    selected_drive_index = int(input("Select a drive (enter the corresponding number): ")) - 1
    selected_drive = drives[selected_drive_index]
    return selected_drive


def create_drivers_folder(selected_drive):
    drivers_folder_path = os.path.join(selected_drive, 'Drivers')
    os.makedirs(drivers_folder_path, exist_ok=True)
    print(f"Drivers folder created at: {drivers_folder_path}")
    return drivers_folder_path


def create_json_file(filename):
    data = {
        "ts_parameters": {
            "fs": 50,
            "qts": 0.5,
            "qes": 0.5,
            "qms": 3.0,
            "vas": 20,
            "sd": 80,
            "xmax": 5,
            "re": 6,
            "le": 0.5,
            "bl": 10,
            "mmd": 20,
            "mms": 25,
            "cms": 0.0001,
            "rmin": 0.1,
            "dmin": 0.15,
            "xmaxlin": 0.01,
            "powerhandling": 50,
            "impedance": 8
        },
        "dimensions": {
            "frame_diameter": 10,
            "cutout_diameter": 9,
            "depth": 5
        }
    }

    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    print(f"JSON file '{filename}' created successfully.")


if __name__ == "__main__":
    selected_drive = list_available_drives()
    drivers_folder_path = create_drivers_folder(selected_drive)

    filename = input("Enter the desired JSON filename (e.g., my_driver.json): ")
    filename = os.path.join(drivers_folder_path, filename)

    create_json_file(filename)
