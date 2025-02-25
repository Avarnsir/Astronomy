import sunpy.map
import matplotlib.pyplot as plt

# Load an SDO image in FITS format
image = sunpy.map.Map('path_to_your_solar_image.fits')

# Display the image
image.plot()
plt.colorbar()
plt.show()