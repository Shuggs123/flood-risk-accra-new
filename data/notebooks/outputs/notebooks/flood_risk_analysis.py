"""
Flood Risk Analysis in Accra, Ghana
Author: Samuel Whizcode De-graft A-champion
Description:
This script demonstrates a basic geospatial workflow for identifying
potential flood risk zones based on river proximity.
"""

import geopandas as gpd
import matplotlib.pyplot as plt

# Load Accra boundary (placeholder path)
accra_boundary = gpd.read_file("../data/accra_boundary.shp")

# Load river data (placeholder path)
rivers = gpd.read_file("../data/accra_rivers.shp")

# Project data for distance calculations
accra_boundary = accra_boundary.to_crs(epsg=32630)
rivers = rivers.to_crs(epsg=32630)

# Create a 500m buffer around rivers
river_buffer = rivers.buffer(500)

# Plot results
fig, ax = plt.subplots(figsize=(8, 8))
accra_boundary.plot(ax=ax, color="none", edgecolor="black")
river_buffer.plot(ax=ax, color="blue", alpha=0.4)

plt.title("Flood Risk Zones Based on River Proximity – Accra, Ghana")
plt.show()

print("Flood risk analysis script executed successfully.")
