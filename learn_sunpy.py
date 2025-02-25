import sunpy.map
from sunpy.net import Fido, attrs as a
from astropy import units as u
# Search for data from SDO AIA 171 Ångström on a specific date
result = Fido.search(a.Time("2022-01-01 00:00", "2022-01-01 01:00"),
                     a.Instrument.aia, 
                     a.Wavelength(171*u.angstrom))
print(result)
# Download the first file from the result
files = Fido.fetch(result[0])
print(files)

