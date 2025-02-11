import sunpy.map
from sunpy.net import Fido, attrs as a
import astropy.units as u

#Search for latest AIA 171 image
results = Fido.search(a.Time('2024-02-01', '2024-02-02'), a.Instrument('AIA'), a.Wavelength(171*u.angstrom))

#Download the file
file_downloaded = Fido.fetch(results[0, 0], path='~/home/dell/Projects/sun_data')

#Load the file
solar_map = sunpy.map.Map(file_downloaded)
solar_map.peek() #Display the image