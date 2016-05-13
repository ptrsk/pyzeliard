# -*- coding: cp949 -*-
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
from shortsword import *

# 인벤토리를 정의
class CharacterScreen:
    "Inventory, magic etc"
    
    def __init__(self,font):
        self.bgimage = pygame.image.load('./pics/characterscreen-1.png').convert()
        self.bgimage.set_colorkey((0,0,0))
        self.font = font

        self.keysnumber = 0
        self.sword = ShortSword(380,160,40,38)

    def draw(self,game):
        game.screen.blit(self.bgimage, (0, 0))
        game.screen.blit(self.sword.image, (self.sword.x, self.sword.y))
        game.screen.blit(self.font.render(self.sword.typetext, 6, (255,255,255)), (self.sword.x+45,self.sword.y))
        game.screen.blit(self.font.render(str(self.keysnumber), 6, (255,255,255)), (420,251))

