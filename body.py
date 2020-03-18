
import pygame
import math


#Colors
BLACK = 0,0,0
BLUE = 135,206,235
GREEN = 124,252,0
RED = 145,40,60
WHITE = 255,255,255

class Body:



    def __init__(self,bodyRadius, bodyWeight,startX,startY):
        self.x=startX
        self.y=startY
        self.xv=0
        self.yv=0
        self.radius=bodyRadius
        self.weight=bodyWeight
        self.circ=pygame.Rect(self.x,self.y,self.radius,self.radius)
        self.gConstant=40

    def setPosition(self,x,y):
        self.x=x
        self.y=y

    def setSpeed(self,x,y):
        self.xv=x
        self.yv=y

    def centerX(self):
        return self.x+0.5*self.radius

    def centerY(self):
        return self.y+0.5*self.radius


    def move_body(self):
        self.x+=self.xv
        self.y+=self.yv

    def draw_body(self,screen):
        self.circ=pygame.Rect(self.x,self.y,self.radius,self.radius)
        pygame.draw.circle(screen,WHITE,(round(self.x),round(self.y)),self.radius)

        
    def distanceToBody(self,other):
        return math.sqrt(pow(abs(self.x-other.x),2)+pow(abs(self.y-other.y),2))
    

    def applyRealGravity(self,other):
        accel=-self.gConstant*other.weight/pow(max(self.distanceToBody(other),30),2)
        self.xv-=math.cos(self.angleToOther(other))*accel 
        self.yv+=math.sin(self.angleToOther(other))*accel 



    def applyGravity(self,other):
        if self.x>other.x:
            self.xv-=0.25
        else:
            self.xv+=0.25

        if self.y>other.y:
            self.yv-=0.25
        else:
            self.yv+=0.25

    def angleToOther(self,other):
        return math.atan2(self.x-other.x,self.y-other.y)+math.pi/2.0


    def reverseVelocity(self):
        self.yv=-self.yv
        self.xv=-self.xv