# -*- coding: utf-8 -*-
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
from gameobject import *

class Exit(Gameobject):
    """
    Exit
    """
    
    def __init__(self, xx,yy,ww,hh,xoffset,yoffset,roomnumber,locationtext):
        # xx :
        # yy :
        # ww :
        # hh :
        # xoffset : no use
        # ypffset : no use
        # roomnumber :
        # locationtext : ��ġ

        Gameobject.__init__(self,xx,yy)
        self.w = ww
        self.h = hh
        #self.hitpoints = 100000000 #FIX else wall/floor disappears

        ### sets x and y in next room
        self.xoffset = xoffset
        self.yoffset = yoffset
        
        self.roomnumber = roomnumber
        self.locationtext = locationtext # 현재는 사용하지않음

    def draw(self, screen, room):
        pass

    def exitp(self, game):
        # 플레이어 위치가 지도에서 상대좌표 위치내에 들어가 있는가?
        # 반환값 : 출구영역내이면 True 아니면 False
        if (game.player.x > self.x + game.room.relativex and
            game.player.x < self.x + game.room.relativex + self.w and
            game.player.y > self.y + game.room.relativey and
            game.player.y < self.y + game.room.relativey + self.h):
            return True
        return False
