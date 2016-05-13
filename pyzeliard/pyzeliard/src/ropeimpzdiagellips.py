
# Copyright (C) Johan Ceuppens 2015 
# Copyright (C) Johan Ceuppens 2010 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import pygame
from pygame.locals import *
from ropeimpzdiag import *
import math

class RopeImpzDiagEllips(RopeImpzDiag):
    "Rope Bridge"
    def __init__(self,xx,yy,aa,bb,radius,imagefilename,r,g,b):
	####FIXME x,y,x,y
       	RopeImpzDiag.__init__(self,xx,yy,xx,yy,imagefilename,r,g,b)

	# the middle x of the ellips x^2+y^2=r^2
	self.x = xx
	self.y = yy	
	# NOTE x^2/a^2 + y^2/b^2 = r^2
	self.a = aa
	self.b = bb

	self.r = radius

	self.i = 0 ## / medridians, / paralells
	self.j = 0###-2*3.14 ## / medridians, / paralells
        self.w = 0 
        self.h = 0 

        self.cx = xx
        self.cy = yy
        
    def lower(self, player):
	# ellips code
	1

    def collide(self, room, player):
	print "px=%d, roomx=%d" % (player.x,self.x+room.relativex)
	if (player.x > self.x+room.relativex and 
		player.x < self.x+room.relativex and
		player.y > self.y+room.relativey and 
		player.y < self.y+room.relativey + self.h):
		return 1
	return 0

    def calcx(self,y):
	return math.sqrt(abs(self.b*self.b*(y*y/self.a*self.a - self.r*self.r)))
    
    def calcy(self,x):
	return math.sqrt(abs(self.b*self.b*(self.r*self.r - x*x/self.a*self.a)))
   
    def drawoncanvas2(self,screen,room):
	color = (255,0,0)
	self.PI = 3.14152829
	self.cz = 100
	self.n = 100
	self.r = 100
		
	i = 0 ## / medridians, / paralells
	j = 0###-2*3.14 ## / medridians, / paralells
	for loopvar in range(0,100): 
		if j < self.n / 2:
			self.theta1 = j*2*self.PI / self.n - self.PI
			self.theta2 = (j+1)*2*self.PI / self.n - self.PI
			if i < self.n:
				self.theta3 = i * 2*self.PI / self.n
				x = math.cos(self.theta2)*math.cos(self.theta3) 
				y = math.sin(self.theta2)*math.sin(self.theta3)
				z = math.sin(self.theta2)
				self.x = x * self.r
				self.y = y * self.r
			###self.z *= self.r
				screen.blit(self.imagepiece, (self.cx+self.x+room.relativex,self.cy+self.y+room.relativey))
		        #### self.stimlibleft.draw(screen, self.cx+self.x+room.relativex,self.cy+self.y+room.relativey)
                        #sleep(.05) # FIX ghost2 sleep
			###pygame.draw.line(pygame.display.get_surface(),color, (self.cx+self.x,self.cy+self.y),(self.cx+self.x,self.cy+self.y))
				i += .9 # FIX .5 
			else:
				i = 0
			j += .9 # FIX .1
		else:
			j = 0

		 
    def drawoncanvas(self, screen, room):
	for i in range(0,100):####FIXME self.x1,self.x2):
		for j in range(0,100):####FIXME self.x1,self.x2):
			print "ellips x=%d y=%d" % (i,self.calcy(i))
			screen.blit(self.imagepiece, (round(self.calcx(i))+room.relativex, round(self.calcy(self.calcx(i)))+room.relativey))
     
