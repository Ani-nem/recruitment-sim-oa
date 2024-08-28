import numpy as np
import math


def final_disk_speed(height: float, length: float, incline: float, mass: float, friction: float, radius: float) -> float:
    """
    Returns the speed of a uniform disk after it reaches the bottom of an inclined slope.

    :param height: the height of the incline (meters)
    :param length: the length of the slope (meters)
    :param incline: the angle of the slope (degrees)
    :param mass: the mass of the ball (kilograms)
    :param friction: kinetic friction coefficient of the slope's surface (0.0 - 1.0)
    :param radius: the radius of the disk (meters)
    :return: the speed of the disk (m/s)
    """

    GRAVITY = 9.81

    potential = GRAVITY * mass * height
    
    velocity = math.sqrt((4*GRAVITY*height)/3)
    return velocity


print(final_disk_speed(10, 15, 30, 2, 0.2, 0.5))