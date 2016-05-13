#-*- coding: cp949 -*-
#완료함

# Copyright (C) Johan Ceuppens 2015
# Copyright (C) Johan Ceuppens 2011
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

import sys
import pygame

from pygame.locals import *


class ScreenC(pygame):

    display_width=640
    display_height=400
    screen = pygame.display.set_mode((display_width, display_height))
    game_name='Zeliard'
    def __init__(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption(self.game_name)  # set title bar
    
    def __new__(self):
        
        
        
        return screen
    
    def __del__(self):
        
        return 1