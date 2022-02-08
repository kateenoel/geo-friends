import math
from dataclasses import dataclass
import numpy as np


# collect user input
# determine number of sites
def get_num_sites():
    while True:
        try:
            num_sites = int(input("Enter the number of sites: "))
            break

        except ValueError:
            print("Try again, that wasn't a number :)")

    print("Thank you! You are interested in finding the geographic midpoint of ", num_sites, " sites")
    return num_sites


# determine site type
def get_site_type():
    print("1. Zip code")
    print("2. Coordinates")
    while True:
        try:
            site_type = int(input("Enter the number associated with your site data type: "))
            break

        except ValueError:
            print("Try again, that wasn't a number :)")

    print("Thanks! You are entering sites in the form of ", site_type)
    return site_type


# determine coordinate type (if applicable)
def get_coord_type():
    print("1. Degrees")
    print("2. Radians")
    while True:
        try:
            coord_type = int(input("Enter the number associated with your coordinate type: "))
            break

        except ValueError:
            print("Try again, that wasn't a number :)")

    print("Thanks! Your coordinates are in the unit of ", coord_type)
    return coord_type


# define coordinate data classes
@dataclass
class DegreeCoordinates:
    latitude: float
    longitude: float


@dataclass
class RadianCoordinates:
    phi: float
    theta: float


# collect site data
def get_site_data(num_sites, site_type, coord_type):
    #  need to add support for zip code inputs
    if site_type == 2:  # site_type = coordinates
        for i in range(num_sites-1):
            while True:
                try:
                    lat = int(input("Enter the latitude of a site: "))
                    lon = int(input("Now enter its longitude: "))
                    if coord_type == 1:  # coord_type = degrees
                        site = DegreeCoordinates(latitude=lat, longitude=lon)
                    else:
                        site = RadianCoordinates(phi=lat, theta=lon)
                    break

                except ValueError:
                    print("Try again, that wasn't a number :)")
    # LEFT OFF HERE
    print("ENTER MESSAGE")
    return site










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
