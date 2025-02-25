from sunpy.net import Fido, attrs as a
import os

#directory
custom_directory = "/home/dell/PythonProjects/Butterfly"
if not os.path.exists(custom_directory):
    os.makedirs(custom_directory)
# Search for sunspot data
result = Fido.search(a.Time('2010-06-01', '2022-01-01'), a.Instrument.hmi, a.Physobs.intensity)
files = Fido.fetch(result)
