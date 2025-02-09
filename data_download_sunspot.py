import os
from sunpy.net import Fido, attrs as a

# Define directory
custom_directory = "/home/dell/PythonProjects/sunpy_data"
if not os.path.exists(custom_directory):
    os.makedirs(custom_directory)

# Query NOAA sunspot number dataset
result = Fido.search(a.Time('1920-01-01', '2023-01-01'), a.Instrument('SOON'))

# Print results
print(result)

# Fetch and download data
if len(result[0]) > 0:  # Check if data is found
    files = Fido.fetch(result, path=os.path.join(custom_directory, "{file}"))
    print("Downloaded files:", files)
else:
    print("No data found. Try adjusting the date range.")
