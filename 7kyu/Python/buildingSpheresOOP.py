'''
Now that we have a Block let's move on to something slightly more complex: a Sphere.

Arguments for the constructor
radius -> integer or float (do not round it)
mass -> integer or float (do not round it)
Methods to be defined
get_radius()       =>  radius of the Sphere (do not round it)
get_mass()         =>  mass of the Sphere (do not round it)
get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
Example
ball = Sphere(2,50)
ball.get_radius() ->       2
ball.get_mass() ->         50
ball.get_volume() ->       33.51032
ball.get_surface_area() -> 50.26548
ball.get_density() ->      1.49208
'''

import math

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
    
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        vol = (4/3)*(math.pi)*(self.radius**3)
        return round(vol, 5)
    
    def get_surface_area(self):
        area = 4*(math.pi)*(self.radius**2)
        return round(area, 5)
    
    # density = mass / volume
    def get_density(self):
        density = self.mass / self.get_volume()
        return round(density, 5)

# radius: 5, mass: 20
sphere = Sphere(5, 20)
print(sphere.get_radius()) # 5
print(sphere.get_mass()) # 20
print(sphere.get_volume()) # 523.6
print(sphere.get_surface_area()) # 314.16
print(sphere.get_density()) # 0.0382
