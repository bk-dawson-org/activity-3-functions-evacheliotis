import math

def getCylinderVolume(radius, height) :
    '''
    This function calculates the volume of a cylinder
    param radius: This is the radius of the cylinder
    param height: This is the height of a cylinder
    return : The function returns the volume of a cylinder
    '''
    volume = math.pi * (radius ** 2)  * height
    return volume 

# Calculates the volume of a cylinder with values 10 and 12
x = getCylinderVolume(10, 12)
y = getCylinderVolume(2, 6)
print (round(x,4))
print (round(y,4))
print(int(x))

def getNumberOfSlices(radius, height, volumeOfSlice) :
    volume = height * (radius ** 2) * math.pi
    numberOfSlices = volume / volumeOfSlice
    return int(numberOfSlices)

# Calculating the number of slices
numberOfSlices1 = getNumberOfSlices(10, 10, 10)
print(numberOfSlices1)
