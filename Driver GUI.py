import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import json


def create_ts_input_boxes(ts_tab):
    label_fs = ttk.Label(ts_tab, text="Fs:")
    entry_fs = ttk.Entry(ts_tab)

    label_qts = ttk.Label(ts_tab, text="Qts:")
    entry_qts = ttk.Entry(ts_tab)

    label_vas = ttk.Label(ts_tab, text="Vas:")
    entry_vas = ttk.Entry(ts_tab)

    label_sd = ttk.Label(ts_tab, text="Sd:")
    entry_sd = ttk.Entry(ts_tab)

    label_qes = ttk.Label(ts_tab, text="Qes:")
    entry_qes = ttk.Entry(ts_tab)

    label_qms = ttk.Label(ts_tab, text="Qms:")
    entry_qms = ttk.Entry(ts_tab)

    label_re = ttk.Label(ts_tab, text="Re:")
    entry_re = ttk.Entry(ts_tab)

    label_le = ttk.Label(ts_tab, text="Le:")
    entry_le = ttk.Entry(ts_tab)

    label_mms = ttk.Label(ts_tab, text="mms:")
    entry_mms = ttk.Entry(ts_tab)

    label_cms = ttk.Label(ts_tab, text="cms:")
    entry_cms = ttk.Entry(ts_tab)

    label_rms = ttk.Label(ts_tab, text="rms:")
    entry_rms = ttk.Entry(ts_tab)

    label_xmax = ttk.Label(ts_tab, text="xmax:")
    entry_xmax = ttk.Entry(ts_tab)

    label_pe = ttk.Label(ts_tab, text="Pe:")
    entry_pe = ttk.Entry(ts_tab)

    entry_fs.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    label_fs.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    entry_qts.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    label_qts.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_vas.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    label_vas.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_sd.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    label_sd.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    entry_qes.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    label_qes.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    entry_qms.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    label_qms.grid(row=5, column=0, padx=10, pady=10, sticky="e")

    entry_re.grid(row=6, column=1, padx=10, pady=10, sticky="w")
    label_re.grid(row=6, column=0, padx=10, pady=10, sticky="e")

    entry_le.grid(row=7, column=1, padx=10, pady=10, sticky="w")
    label_le.grid(row=7, column=0, padx=10, pady=10, sticky="e")

    entry_mms.grid(row=8, column=1, padx=10, pady=10, sticky="w")
    label_mms.grid(row=8, column=0, padx=10, pady=10, sticky="e")

    entry_cms.grid(row=9, column=1, padx=10, pady=10, sticky="w")
    label_cms.grid(row=9, column=0, padx=10, pady=10, sticky="e")

    entry_rms.grid(row=10, column=1, padx=10, pady=10, sticky="w")
    label_rms.grid(row=10, column=0, padx=10, pady=10, sticky="e")

    entry_xmax.grid(row=11, column=1, padx=10, pady=10, sticky="w")
    label_xmax.grid(row=11, column=0, padx=10, pady=10, sticky="e")

    entry_pe.grid(row=12, column=1, padx=10, pady=10, sticky="w")
    label_pe.grid(row=12, column=0, padx=10, pady=10, sticky="e")


def create_dimensions_input_boxes(dimensions_tab):
    label_outer_width = ttk.Label(dimensions_tab, text="Outer Width:")
    entry_outer_width = ttk.Entry(dimensions_tab)

    label_outer_ring_thickness = ttk.Label(dimensions_tab, text="Outer Ring Thickness:")
    entry_outer_ring_thickness = ttk.Entry(dimensions_tab)

    label_od_of_surround = ttk.Label(dimensions_tab, text="OD of Surround:")
    entry_od_of_surround = ttk.Entry(dimensions_tab)

    label_id_of_surround = ttk.Label(dimensions_tab, text="ID of Surround:")
    entry_id_of_surround = ttk.Entry(dimensions_tab)

    label_surround_thickness = ttk.Label(dimensions_tab, text="Surround Thickness:")
    entry_surround_thickness = ttk.Entry(dimensions_tab)

    label_outer_diameter_of_spider = ttk.Label(dimensions_tab, text="Outer Diameter of Spider:")
    entry_outer_diameter_of_spider = ttk.Entry(dimensions_tab)

    label_inner_diameter_of_spider = ttk.Label(dimensions_tab, text="Inner Diameter of Spider:")
    entry_inner_diameter_of_spider = ttk.Entry(dimensions_tab)

    label_spider_thickness = ttk.Label(dimensions_tab, text="Spider Thickness:")
    entry_spider_thickness = ttk.Entry(dimensions_tab)

    label_outer_diameter_of_coil_former = ttk.Label(dimensions_tab, text="Outer Diameter of Coil Former:")
    entry_outer_diameter_of_coil_former = ttk.Entry(dimensions_tab)

    label_inner_diameter_of_coil_former = ttk.Label(dimensions_tab, text="Inner Diameter of Coil Former:")
    entry_inner_diameter_of_coil_former = ttk.Entry(dimensions_tab)

    label_coil_former_thickness = ttk.Label(dimensions_tab, text="Coil Former Thickness:")
    entry_coil_former_thickness = ttk.Entry(dimensions_tab)

    label_mounting_depth = ttk.Label(dimensions_tab, text="Mounting Depth:")
    entry_mounting_depth = ttk.Entry(dimensions_tab)

    label_magnet_diameter = ttk.Label(dimensions_tab, text="Magnet Diameter:")
    entry_magnet_diameter = ttk.Entry(dimensions_tab)

    label_magnet_thickness = ttk.Label(dimensions_tab, text="Magnet Thickness:")
    entry_magnet_thickness = ttk.Entry(dimensions_tab)

    label_magnet_weight = ttk.Label(dimensions_tab, text="Magnet Weight:")
    entry_magnet_weight = ttk.Entry(dimensions_tab)

    label_magnet_gap_height = ttk.Label(dimensions_tab, text="Magnet Gap Height:")
    entry_magnet_gap_height = ttk.Entry(dimensions_tab)

    label_magnet_gap_diameter = ttk.Label(dimensions_tab, text="Magnet Gap Diameter:")
    entry_magnet_gap_diameter = ttk.Entry(dimensions_tab)

    label_magnet_gap_thickness = ttk.Label(dimensions_tab, text="Magnet Gap Thickness:")
    entry_magnet_gap_thickness = ttk.Entry(dimensions_tab)

    label_magnet_gap_length = ttk.Label(dimensions_tab, text="Magnet Gap Length:")
    entry_magnet_gap_length = ttk.Entry(dimensions_tab)

    label_cutout_diameter = ttk.Label(dimensions_tab, text="Cutout Diameter:")
    entry_cutout_diameter = ttk.Entry(dimensions_tab)

    entry_outer_width.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    label_outer_width.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    entry_outer_ring_thickness.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    label_outer_ring_thickness.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_id_of_surround.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    label_id_of_surround.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_surround_thickness.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    label_surround_thickness.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    entry_outer_diameter_of_spider.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    label_outer_diameter_of_spider.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    entry_inner_diameter_of_spider.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    label_inner_diameter_of_spider.grid(row=5, column=0, padx=10, pady=10, sticky="e")

    entry_spider_thickness.grid(row=6, column=1, padx=10, pady=10, sticky="w")
    label_spider_thickness.grid(row=6, column=0, padx=10, pady=10, sticky="e")

    entry_outer_diameter_of_coil_former.grid(row=7, column=1, padx=10, pady=10, sticky="w")
    label_outer_diameter_of_coil_former.grid(row=7, column=0, padx=10, pady=10, sticky="e")

    entry_inner_diameter_of_coil_former.grid(row=8, column=1, padx=10, pady=10, sticky="w")
    label_inner_diameter_of_coil_former.grid(row=8, column=0, padx=10, pady=10, sticky="e")

    entry_coil_former_thickness.grid(row=9, column=1, padx=10, pady=10, sticky="w")
    label_coil_former_thickness.grid(row=9, column=0, padx=10, pady=10, sticky="e")

    entry_mounting_depth.grid(row=10, column=1, padx=10, pady=10, sticky="w")
    label_mounting_depth.grid(row=10, column=0, padx=10, pady=10, sticky="e")

    entry_magnet_diameter.grid(row=11, column=1, padx=10, pady=10, sticky="w")
    label_magnet_diameter.grid(row=11, column=0, padx=10, pady=10, sticky="e")

    entry_magnet_thickness.grid(row=12, column=1, padx=10, pady=10, sticky="w")
    label_magnet_thickness.grid(row=12, column=0, padx=10, pady=10, sticky="e")

    entry_magnet_weight.grid(row=13, column=1, padx=10, pady=10, sticky="w")
    label_magnet_weight.grid(row=13, column=0, padx=10, pady=10, sticky="e")

    entry_magnet_gap_height.grid(row=14, column=1, padx=10, pady=10, sticky="w")
    label_magnet_gap_height.grid(row=14, column=0, padx=10, pady=10, sticky="e")

    entry_magnet_gap_diameter.grid(row=15, column=1, padx=10, pady=10, sticky="w")
    label_magnet_gap_diameter.grid(row=15, column=0, padx=10, pady=10, sticky="e")

    entry_magnet_gap_thickness.grid(row=16, column=1, padx=10, pady=10, sticky="w")
    label_magnet_gap_thickness.grid(row=16, column=0, padx=10, pady=10, sticky="e")

    entry_magnet_gap_length.grid(row=17, column=1, padx=10, pady=10, sticky="w")
    label_magnet_gap_length.grid(row=17, column=0, padx=10, pady=10, sticky="e")

    entry_cutout_diameter.grid(row=18, column=1, padx=10, pady=10, sticky="w")
    label_cutout_diameter.grid(row=18, column=0, padx=10, pady=10, sticky="e")

    entry_od_of_surround.grid(row=19, column=1, padx=10, pady=10, sticky="w")
    label_od_of_surround.grid(row=19, column=0, padx=10, pady=10, sticky="e")


def create_thermal_input_boxes(thermal_tab):
    label_power = ttk.Label(thermal_tab, text="Power:")
    entry_power = ttk.Entry(thermal_tab)

    label_thermal_resistance = ttk.Label(thermal_tab, text="Thermal Resistance:")
    entry_thermal_resistance = ttk.Entry(thermal_tab)

    label_ambient_temperature = ttk.Label(thermal_tab, text="Ambient Temperature:")
    entry_ambient_temperature = ttk.Entry(thermal_tab)

    label_voice_coil_diameter = ttk.Label(thermal_tab, text="Voice Coil Diameter:")
    entry_voice_coil_diameter = ttk.Entry(thermal_tab)

    label_voice_coil_length = ttk.Label(thermal_tab, text="Voice Coil Length:")
    entry_voice_coil_length = ttk.Entry(thermal_tab)

    label_voice_coil_height = ttk.Label(thermal_tab, text="Voice Coil Height:")
    entry_voice_coil_height = ttk.Entry(thermal_tab)

    label_voice_coil_overhang = ttk.Label(thermal_tab, text="Voice Coil Overhang:")
    entry_voice_coil_overhang = ttk.Entry(thermal_tab)

    entry_thermal_resistance.grid(row=0, column=1, padx=10, pady=10, sticky="w")
    label_thermal_resistance.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    entry_ambient_temperature.grid(row=1, column=1, padx=10, pady=10, sticky="w")
    label_ambient_temperature.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    entry_voice_coil_diameter.grid(row=2, column=1, padx=10, pady=10, sticky="w")
    label_voice_coil_diameter.grid(row=2, column=0, padx=10, pady=10, sticky="e")

    entry_voice_coil_length.grid(row=3, column=1, padx=10, pady=10, sticky="w")
    label_voice_coil_length.grid(row=3, column=0, padx=10, pady=10, sticky="e")

    entry_voice_coil_height.grid(row=4, column=1, padx=10, pady=10, sticky="w")
    label_voice_coil_height.grid(row=4, column=0, padx=10, pady=10, sticky="e")

    entry_voice_coil_overhang.grid(row=5, column=1, padx=10, pady=10, sticky="w")
    label_voice_coil_overhang.grid(row=5, column=0, padx=10, pady=10, sticky="e")

    entry_power.grid(row=6, column=1, padx=10, pady=10, sticky="w")
    label_power.grid(row=6, column=0, padx=10, pady=10, sticky="e")


class DriverConfiguratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Driver Configurator")
        self.master.geometry("1200x900")

        self.configurations = {}

        self.create_tabs()

    def create_tabs(self):
        tab_parent = ttk.Notebook(self.master)

        ts_tab = ttk.Frame(tab_parent)
        dimensions_tab = ttk.Frame(tab_parent)
        thermal_tab = ttk.Frame(tab_parent)
        save_tab = ttk.Frame(tab_parent)

        tab_parent.add(ts_tab, text="TS")
        tab_parent.add(dimensions_tab, text="Dimensions")
        tab_parent.add(thermal_tab, text="Thermal")
        tab_parent.add(save_tab, text="Save")

        create_ts_input_boxes(ts_tab)
        create_dimensions_input_boxes(dimensions_tab)
        create_thermal_input_boxes(thermal_tab)
        self.create_save_tab(save_tab)

        tab_parent.pack(expand=1, fill='both')

    def create_save_tab(self, tab):
        # Create input boxes for brand and model
        label_brand = ttk.Label(tab, text="Brand:")
        entry_brand = ttk.Entry(tab)

        label_model = ttk.Label(tab, text="Model:")
        entry_model = ttk.Entry(tab)

        label_brand.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        entry_brand.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        label_model.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        entry_model.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Create Save button
        save_button = (ttk.Button
                       (tab, text="Save", command=lambda: self.save_configuration
                        (entry_brand.get(), entry_model.get())))
        save_button.grid(row=2, column=0, columnspan=2, pady=20)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )

        if file_path:
            with open(file_path, "w") as file:
                json.dump(self.configurations, file, indent=4)

    def save_configuration(self, brand, model):
        if not brand or not model:
            messagebox.showerror("Error", "Brand and model are required")
            return

        self.configurations[brand] = model
        self.save_file()


def main():
    root = tk.Tk()
    app = DriverConfiguratorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
