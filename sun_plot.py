import sunpy.map
import matplotlib.pyplot as plt
from astropy.visualization import AsinhStretch, ImageNormalize
import os

# Define the custom directory
custom_directory = "/home/dell/PythonProjects/sun_data"

# Find all .fits files in the directory
fits_files = [file for file in os.listdir(custom_directory) if file.endswith(".fits")]

# Load the first .fits file
if fits_files:
    file_path = os.path.join(custom_directory, fits_files[0])
    smap = sunpy.map.Map(file_path)
    print(f"Loaded file: {custom_directory}")

    # Plot the solar data
    plt.figure(figsize=(10, 8))
    norm = ImageNormalize(smap.data, stretch=AsinhStretch(0.1))
    smap.plot(norm=norm, cmap='sdoaia304')  # Choose the colormap matching the wavelength
    plt.colorbar(label='Intensity')
    plt.title(f"Solar Image from {smap.date}")
    plt.show()
else:
    print("No .fits files found in the specified directory.")
