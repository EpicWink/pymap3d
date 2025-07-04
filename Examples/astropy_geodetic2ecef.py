#!/usr/bin/env python3

"""
https://github.com/geospace-code/pymap3d/issues/103
"""

from datetime import datetime
import sys

from astropy.time import Time
import astropy
import pymap3d as pm

print("Python version:", sys.version)
print("AstroPy version:", astropy.__version__)

lat = 33.6  # deg
lon = 134.3  # deg
alt = 0  # m

dt = datetime(2020, 8, 14, 0, 0, 41)

# %% Astropy time for comparison
astropy_time = Time(dt, scale="utc")
print("----------------------------------------")
print("Astropy Time (UTC):", astropy_time.utc)
print("Julian Date (UTC):", astropy_time.utc.jd)
print("Julian Date (TT):", astropy_time.tt.jd)
print("GMST:", astropy_time.sidereal_time("mean", "greenwich"))

# %% 1. Geodetic to ECEF
ecef = pm.geodetic2ecef(lat, lon, alt)
print("\nECEF Coordinates (meters):")
print(f"X: {ecef[0]:.8f}, Y: {ecef[1]:.8f}, Z: {ecef[2]:.8f}")

# %% 2. ECEF to ECI (J2000)
eci = pm.ecef2eci(ecef[0], ecef[1], ecef[2], dt)
print("\nECI Coordinates (meters):")
print(f"X: {eci[0]}, Y: {eci[1]}, Z: {eci[2]}")
