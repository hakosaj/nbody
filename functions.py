
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

