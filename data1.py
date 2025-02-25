from sunpy.net import Fido, attrs as a
import os

# Custom directory
custom_directory = "/home/dell/PythonProjects/Butterfly"
if not os.path.exists(custom_directory):
    os.makedirs(custom_directory)

# Search for sunspot data with a broader query
try:
    result = Fido.search(
        a.Time('2015-01-01', '2015-12-31'),  # Time range
        a.Instrument.hmi,                    # Instrument
        a.Physobs.intensity                # Physical observable
    )
    
    print(f"Found {len(result)} files to download.")
    
    # Fetch files and save to custom directory
    if len(result) > 0:
        files = Fido.fetch(result, path=os.path.join(custom_directory, '{file}'))
        print(f"Downloaded files: {files}")
    else:
        print("No files found for the given query. Try adjusting the search parameters.")
except Exception as e:
    print(f"An error occurred: {e}")
