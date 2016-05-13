
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

class RopeImpzDiagSinus(RopeImpzDiag):
    "Rope Bridge"
    def __init__(self,x1,y1,x2,y2,theta,dtheta,dy,imagefilename,r,g,b):
       	RopeImpzDiag.__init__(self,x1,y1,x2,y2,imagefilename,r,g,b)

	self.starttheta = theta
	self.PI = 3.14152829
	self.theta = theta
	self.dtheta = dtheta
	self.dy = dy

    def lower(self, player):
	# ellips code
	1

    def collide(self, room, player):
	### print "px=%d, roomx=%d" % (player.x,self.x+room.relativex)
	if (player.x > min(self.x1,self.x2)+room.relativex and 
		player.x < max(self.x1,self.x2)+room.relativex and
		player.y > min(self.y1,self.y2)+room.relativey and
		### FIXME abs below 
		player.y < min(self.y1,self.y2)+room.relativey + abs(self.y1-self.y2)):
		return 1
	return 0

    def drawon(self, screen, room):
	self.theta = self.starttheta 
	for i in range(0,400):
		###print "sinus x=%d y=%d" % (i,math.sin(self.theta)*10)
		screen.blit(self.imagepiece, (min(self.x1,self.x2)+i+room.relativex, math.sin(self.theta)*self.dy+min(self.y1,self.y2)+room.relativey))
    		self.theta += self.dtheta 
		i += 9 
