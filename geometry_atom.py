import os 
import numpy
import sys

def calculate_distance(coords1, coords2):
    """
    This function has two arguments, the coordinates of two atoms. It returns the distance between atoms.
    """
    x_distance = coords1[0] - coords2[0]
    y_distance = coords1[1] - coords2[1]
    z_distance = coords1[2] - coords1[2]
    distance_12 = numpy.sqrt(x_distance**2 + y_distance**2 + z_distance**2)
    return distance_12
    
def bond_check(distance,minimum=0,maximum=1.5):
    """
    Checks a distance to see if its a bond
    """
    if distance>minimum and distance<maximum:
        return True
    else:
        return False 
        
        
file_location = sys.argv[1]
xyz_file = numpy.genfromtxt(fname=file_location, skip_header=2, dtype='unicode')
symbols = xyz_file[:,0]
coordinates = xyz_file[:,1:]
#print(symbols)
#print(coordinates)
coordinates = coordinates.astype(numpy.float)

num_atoms = len(symbols)
for num1 in range(0,num_atoms):
    for num2 in range(0,num_atoms):
        if num1>num2:               
            distance_12 = calculate_distance(coordinates[num1], coordinates[num2])
            if bond_check(distance_12, maximum=2.0) is True:
                print(F'{symbols[num1]} to {symbols[num2]} : {distance_12:.3f}')