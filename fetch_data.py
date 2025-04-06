import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import fastf1 as ff1
import pandas as pd
import json

# read the json config file
config = json.load(open('config.json'))
YEAR = config['year']
GP = config['gp']
SESSION_TYPE = config['session_type']
DRIVER_ABBRV = config['driver_abbrv']

# Fetch the session object
session = ff1.get_session(year=YEAR, gp=GP, identifier=SESSION_TYPE)
# This function will return a Session object, but it will not load any session specific data like lap timing, telemetry... yet.
# For this, you will need to call load() function on the returned object.
session.load(telemetry=True)

# Fetch the Laps object for the specified driver
single_driver_all_laps = session.laps.pick_drivers(DRIVER_ABBRV)
single_driver_fastest_lap = single_driver_all_laps.pick_fastest()
single_driver_fastest_lap.telemetry.to_csv(f'{DRIVER_ABBRV}_{YEAR}_{GP}_{SESSION_TYPE}_{str(single_driver_fastest_lap['LapTime']).replace(':','_').replace('0 days 00_','').replace('.','_')}.csv', index=False)


# Sample data (replace with your actual coordinates)
x = single_driver_fastest_lap.telemetry['X']
y = single_driver_fastest_lap.telemetry['Y']
z = single_driver_fastest_lap.telemetry['Z']

# Create the figure and 3D axes
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Create the scatter plot
ax.scatter(x, y, z, c='blue', marker='o')  # 'c' for color, 'marker' for point style

# Set axis labels
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')

# Set the view to be along the z-axis, this will give a top-down view
ax.view_init(elev=90, azim=0)

# Set title
plt.title('3D Scatter Plot')

# Save the plot
plt.savefig(f'{DRIVER_ABBRV}_{YEAR}_{GP}_{SESSION_TYPE}_{str(single_driver_fastest_lap['LapTime']).replace(':','_').replace('0 days 00_','').replace('.','_')}.png')

# Show the plot
plt.show()