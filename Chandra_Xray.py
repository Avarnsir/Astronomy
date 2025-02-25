from astroquery.csc import Catalogs
result = Catalogs.query_region("Abell 2029", radius="5 arcmin", catalog="chandra_obs")