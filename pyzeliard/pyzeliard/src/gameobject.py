# -*- coding: cp949 -*-
# Copyright (C) Johan Ceuppens 2015
# Copyright (C) Johan Ceuppens 2014
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
import random 
import math 
from rng import *

class Gameobject:
    "Game object"
    def __init__(self, xx,yy):
        self.x = xx 
        self.y = yy
        # default width and height 
        self.w = 48
        self.h = 48
        #self.SCREENH = 640 #안쓰는것같아서 닫음
        #self.SCREENW = 400
        self.rng = RNG(self)
     
        self.playerimageyoffset = 15
 
    def getrng(self):
        print "getrng - no use"
        return self.rng
 
    def draw(self, screen, room):
        print "draw - no use"
        screen.blit(self.image,(self.x+room.relativex,self.y+room.relativey))

    def hitwithplayer(self,player):
        self.hitpoints -= self.getrng().rollplayersword(player)

    def fallcollide(self, room, player):
        # 낙하충돌 확인
        # 반환 : 점프중= 0 바닥에있으면= 1
        
        # FIX BUG
        #print("player.y" , player.y,)
        #print("room.relativey" , room.relativey) #점프시 이값만 바뀜
        #print("player.h" , player.h )
        #print("self.playerimageyoffset", self.playerimageyoffset)
        #print("self.y", self.y) 
        if (player.y-room.relativey+player.h-self.playerimageyoffset >= self.y and 
            player.y-room.relativey+player.h-self.playerimageyoffset <= self.y + self.h and
            player.x-room.relativex >= self.x and 
            player.x-room.relativex <= self.x+self.w):
            #print "FALL collision with Game Object!"
            #print "게임 객체와 낙하 충돌!"
            return True 
        else:
            #print "점프중. ## for game self.talker"
            return False ## for game self.talker

    def collide(self, room, player):	
        if (player.x-room.relativex >= self.x  and 
	player.x-room.relativex <= self.x+self.w and 
	player.y-room.relativey >= self.y-self.h and #FIXED +self.h
	player.y-room.relativey <= self.y+self.h):
	    #print "collision in gameobject!"	
	    return 2 
	else:
	    return 0

    def collideX(self, room, player):
        if (player.x-room.relativex >= self.x  and 
	player.x-room.relativex <= self.x+self.w):
	    return 5 #FIXME1 check for previous return 2
	else:
	    return 0

    def collideY(self, room, player):
        if (player.y-room.relativey >= self.y  and 
	player.y-room.relativey <= self.y+self.w):
	    return 5 #FIXME1 check for previous return 2
	else:
	    return 0

    def collideundomove(self, room, player):
	if self.collideX(room, player) == 5 and self.collideY(room,player) == 5:
		return self	
	else:
		return None

    def collideXY(self, room, player):
	if player.direction == "right":
		if (player.x+player.w > self.x  and 
		player.x < self.x+self.w and 
		player.y+player.h > self.y and 
		player.y-player.h < self.y+max(player.h, self.h)+1):
			return 5 
	elif player.direction == "left":
		if (player.x+player.w > self.x  and 
		player.x < self.x+self.w and 
		player.y+player.h > self.y and 
		player.y-player.h < self.y+max(player.h, self.h)+1):
			return 5 
	else:
		return 0

    def collideobjectX(self, room):
	for i in room.gameobjects:
	    if i != None and i != self:	
	        if (self.x > i.x  and 
		    self.x < i.x+i.w):
	            return 1 
	return 0

    def collideobjectY(self, room):
	for i in room.gameobjects:
	    if i != None and i != self:	
	        if (self.y-self.h > i.y  and 
		    self.y < i.y+i.h):
	            return 1 
	return 0
 
    def collideobjectXY(self, room,player):
	for i in room.gameobjects:
	    if i and i != self:		
	        if (self.x > i.x  and 
	 	    self.x < i.x+i.w and 
	            self.y+self.h > i.y and 
	            self.y-self.h < i.y+max(self.h, i.h)+1):
	            return 1 
	return 0 
    
    def update(self,room,player):
	1

    def fight(self,room,player):
	1
    
    def undomove(self):
	1

