
import sys
import os
import random
import time
import pygame
import numpy as np
import math
import pygame
import math
from body import Body

def allGravities(bodies):
    for body in bodies:
        for body2 in bodies:
            if body2!=body:
                body.applyRealGravity(body2)

def centreOfMass(bodies):
    totalMass = sum(list(map(lambda x:x.weight,bodies)))
    xm = sum(list(map(lambda n:n.weight*n.x,bodies)))/totalMass
    ym = sum(list(map(lambda n:n.weight*n.y,bodies)))/totalMass
    print(f"center: {xm},{ym}")
    return xm,ym

