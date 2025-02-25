from astroquery.sdss import SDSS
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

# Select a specific star (change plate, mjd, fiberid as needed)
plate = 2668
mjd = 54265
fiberid = 114

# Download the spectrum
sp = SDSS.get_spectra(plate=plate, fiberID=fiberid, mjd=mjd)

# Save the FITS file locally
if sp:
    sp.writeto("star_spectrum.fits", overwrite=True)
    print("Spectrum downloaded successfully!")
else:
    print("No data found.")
# Open the FITS file
hdu = fits.open("star_spectrum.fits")

# Print the FITS header information
hdu.info()
