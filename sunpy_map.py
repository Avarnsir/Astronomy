import os

import matplotlib.pyplot as plt

import astropy.units as u

import sunpy.map
from sunpy.net import Fido
from sunpy.net import attrs as a
jsoc_email = "avarnn1827@gmail.com"

result = Fido.search(a.Time("2011-03-09 23:20:00", "2011-03-09 23:30:00"),
                     a.Sample(1*u.hour),
                     a.jsoc.Series("hmi.sharp_cea_720s"),
                     a.jsoc.PrimeKey("HARPNUM", 401),
                     a.jsoc.Notify(jsoc_email),
                     a.jsoc.Segment("Bp"))
print(result)
file = Fido.fetch(result)
sharp_map = sunpy.map.Map(file)
fig = plt.figure()
ax = fig.add_subplot(projection=sharp_map)
sharp_map.plot(axes=ax, vmin=-1500, vmax=1500)

plt.show()
