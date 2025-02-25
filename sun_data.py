from sunpy.net import Fido, attrs as a
from astropy import units as u
import os

# Coustom directory
custom_directory ="/home/dell/PythonProjects/sun_data"
if not os.path.exists(custom_directory):
  os.markdirs(custom_directory)
# Search for data
results = Fido.search(a.Time("2012-07-13 16:00", "2012-07-13 16:10"),
                      a.Instrument.aia,
                      a.Wavelength(171 * u.angstrom))
print(results)
# Download data
files = Fido.fetch(results[:3], path=os.path.join(custom_directory, "{file}"))
print(files)
