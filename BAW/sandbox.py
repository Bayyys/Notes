from shapely.geometry import Polygon
import numpy as np
import math

def regular_pentagon_from_area(area):
    # Calculate side length from area
    s = math.sqrt(4 * area * math.tan(math.pi / 5) / 5)
    
    # Calculate the radius of the circumscribed circle
    r = s / (2 * math.sin(math.pi / 5))
    
    # Generate the regular pentagon coordinates
    coords = []
    for i in range(5):
        angle = 2 * math.pi * i / 5
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        coords.append((x, y))
    
    return Polygon(coords)

# Example usage
area = 25
pentagon = regular_pentagon_from_area(area)
print(pentagon)
print("Area:", pentagon.area)


from shapely.geometry import Polygon
import math

def scale_pentagon_to_area(pentagon, desired_area):
    # Calculate the current area
    original_area = pentagon.area
    
    # Calculate the scale factor
    scale_factor = math.sqrt(desired_area / original_area)
    
    # Calculate the centroid of the pentagon
    centroid = pentagon.centroid
    
    # Create a new pentagon by scaling each vertex relative to the centroid
    scaled_coords = [(centroid.x + scale_factor * (x - centroid.x),
                      centroid.y + scale_factor * (y - centroid.y)) for x, y in pentagon.exterior.coords[:-1]]
    
    return Polygon(scaled_coords)

# Example usage
area = 25
pentagon = regular_pentagon_from_area(10)  # Using the function from before
scaled_pentagon = scale_pentagon_to_area(pentagon, area)
print(scaled_pentagon)
print("Desired Area:", area)
print("Actual Area:", scaled_pentagon.area)


from shapely.geometry import Polygon

def mirror_across_centroid(polygon):
    centroid_x = polygon.centroid.x
    mirrored_coords = [(2*centroid_x - x, y) for x, y in polygon.exterior.coords[:-1]]
    return Polygon(mirrored_coords)

# Example usage
pentagon = Polygon([(1, 1), (2, 3), (3, 2), (3, 0), (1, 0)])
mirrored_pentagon = mirror_across_centroid(pentagon)
print(mirrored_pentagon)


from shapely.geometry import Polygon
import math

def compute_angle(A, B, C):
    # Vectors
    AB = [B[0]-A[0], B[1]-A[1]]
    BC = [C[0]-B[0], C[1]-B[1]]
    
    # Dot product
    dot_product = AB[0]*BC[0] + AB[1]*BC[1]
    
    # Magnitudes
    mag_AB = math.sqrt(AB[0]**2 + AB[1]**2)
    mag_BC = math.sqrt(BC[0]**2 + BC[1]**2)
    
    # Angle in radians
    angle = math.acos(dot_product / (mag_AB * mag_BC))
    
    # Convert to degrees
    angle_deg = math.degrees(angle)
    return angle_deg

def get_angles(pentagon):
    coords = list(pentagon.exterior.coords[:-1])  # Exclude the repeated last coordinate
    angles = []
    
    for i in range(5):
        A = coords[i-1]
        B = coords[i]
        C = coords[(i+1)%5]
        angles.append(compute_angle(A, B, C))
    
    return angles

# Example usage:
pentagon = Polygon([(0, 0), (2, 3), (5, 3), (7, 0), (5, -3)])
angles = get_angles(pentagon)
print(angles)
print(np.sum(angles))





