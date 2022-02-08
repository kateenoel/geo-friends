import math
import numpy as np

# collect user input
def collect_information():
    num_sites = int(input("Enter number of sites: "))



# calculate geographic midpoint
# create list of latitude, longitude tuples for each location of interest
L = [(44.9778, 93.2650),
     (33.7490, 84.3880),
     (42.3601, 71.0589)]


# convert latitude, longitude coordinates to radians
def coords_to_radians(site):
    latitude = site[0]
    longitude = site[1]
    lat_rad = math.radians(latitude)
    lon_rad = math.radians(longitude)
    return lat_rad, lon_rad


# convert latitude, longitude to cartesian
def radians_to_cartesian(site):
    lat_rad = site[0]
    lon_rad = site[1]
    x = math.cos(lat_rad)*math.cos(lon_rad)
    y = math.cos(lat_rad)*math.sin(lon_rad)
    z = math.sin(lat_rad)
    return x, y, z

# add in weights (later)


# compute (optionally weighted) mean cartesian points
xs = [coord[0] for coord in cartesian]
ys = [coord[1] for coord in cartesian]
zs = [coord[2] for coord in cartesian]

mean_x = sum(xs)/len(xs)
mean_y = sum(ys)/len(ys)
mean_z = sum(zs)/len(zs)

# convert cartesian points back to latitude, longitude
lon = np.degrees(np.arctan2(mean_y, mean_x))
hyp = np.sqrt(mean_x*mean_x + mean_y*mean_y)
lat = np.degrees(np.arctan2(mean_z, hyp))

print(lat)
print(lon)
