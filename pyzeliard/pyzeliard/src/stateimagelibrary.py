# -*- coding: cp949 -*-
#!/usr/local/bin/python
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

from time import *
from pygame.time import delay

class Stateimagelibrary:
    def __init__(self):
        self.index = 0
        self.max = 0
        self.list = []
    
    def addpicture(self, image):
        self.list.append(image)
        self.max += 1

    def drawstatic(self, screen, xx, yy, index):
        """
        Ư�� ����
        """
        if (self.index >= self.max):
            self.index = 0

        screen.blit(self.list[index],(xx,yy)) 

    def drawstatic(self, screen, xx, yy):
        """
        ���� ����
        """
        if (self.index >= self.max):
            self.index = 0

        screen.blit(self.list[self.index],(xx,yy)) 

    def draw(self, screen, xx, yy):
        """
        ���� ���� - �Ⱦ�
        """
        if (self.index >= self.max):
            self.index = 0

        screen.blit(self.list[self.index],(xx,yy)) 
        self.index += 1
        sleep(0.1)

    def draw(self, screen, xx, yy, delay_time):
        """
        ���� ���� �����ð����Ե�.
        """
        if (self.index >= self.max):
            self.index = 0

        screen.blit(self.list[self.index],(xx,yy)) 
        self.index += 1
        sleep(delay_time)
