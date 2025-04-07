import bpy
import csv
import os

# Get the path of the current script or blend file
script_path = os.path.dirname(bpy.data.filepath)
csv_file = os.path.join(script_path, "ANT_2025_japan_R_01_30_965000_coordinates.csv")

# Read the coordinates from the CSV file
coordinates = []
with open(csv_file, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        x = float(row['x'])/100
        y = float(row['y'])/100
        z = float(row['z'])/100
        coordinates.append((x, y, z))

# Create a new curve
curve_data = bpy.data.curves.new(name='PathCurve', type='CURVE')
curve_data.dimensions = '3D'

# Create a new spline and add the points
spline = curve_data.splines.new(type='POLY')
spline.points.add(len(coordinates) - 1)  # add() adds N more points
for i, coord in enumerate(coordinates):
    spline.points[i].co = (*coord, 1)  # Bezier points use (x, y, z, w)

# Create a new object with the curve
curve_obj = bpy.data.objects.new('PathObject', curve_data)
bpy.context.collection.objects.link(curve_obj)

print("Path created from CSV!")
