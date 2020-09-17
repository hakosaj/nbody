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
from functions import allGravities, centreOfMass

#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 145,40,60
WHITE = 255,255,255

#Initialize pygame
pygame.init()
pygame.font.init()
start_time = None
clock = pygame.time.Clock ()

#Screen size
width,height=1200,900
size = width,height


#Screen objects
screen = pygame.display.set_mode(size)
pygame.display.set_caption("N-BodyProblem")

p1 = Body(10,10,300,300)
p1.setSpeed(-0.1,-0.1)
p2 = Body(10,10,700,300)
p2.setSpeed(0.4,-0.1)
p3 = Body(10,10,400,500)
p3.setSpeed(-0.5,0.1)
p4 = Body(10,10,250,500)
p4.setSpeed(0.2,0.1)
#bodies=[p1,p2,p3]
bodies=[p1,p2,p3,p4]
ticks=1

xm,ym = centreOfMass(bodies)
while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    
    screen.fill(BLACK)

    allGravities(bodies)

    if ticks%30==0:
        xm,ym=centreOfMass(bodies)
        ticks=0
    


    
    #Draw centre of gravity
    r=pygame.Rect(round(xm),round(ym),10,10)
    pygame.draw.rect(screen,WHITE,r)
    
    
    
    for body in bodies:
        body.move_body()
        body.draw_body(screen)

    pygame.display.flip()

    clock.tick(240)
    ticks+=1