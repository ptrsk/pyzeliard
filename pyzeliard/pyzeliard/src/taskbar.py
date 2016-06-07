# -*- coding: utf-8 -*-
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
from color import *


# 하단의 상태표시줄
class Taskbar:
    "Taskbar"

    # 상태창
    # screen :
    # font : 폰트
    # player :
    def __init__(self, screen, font, player):
        self.screen = screen
        self.font = font
        self.player = player

        # 칼 이미지
        self.swordimage = pygame.image.load('./pics/sword1-40x38.png').convert()  # 칼모양
        self.swordimage.set_colorkey(Colors.PURPLE)  # 보라색?
        self.sword = ShortSword(384, 341, 40, 38)

        self.image = pygame.image.load('./pics/taskbar.png').convert()  # 상태창
        self.image.set_colorkey(Colors.RED)  # 빨간색

        self.goldnumber = 0  # 돈초기화
        self.almasnumber = 0  # 알마스 초기화

    def draw(self, game):
        # TODO: 나중엔 그냥 전부 그릴것
        pygame.draw.rect(game.screen, Colors.WHITE, (96, 316, 744, 2)) # 흰색경계선
        pygame.draw.rect(game.screen, Colors.GRAY, (96, 318, 744, 138)) # 배경색
        game.screen.blit(self.image, (70, 310))

        game.screen.blit(self.font.render(u'LIFE', True, Colors.TITLE), (105, 325))

        game.screen.blit(self.sword.image, (self.sword.x, self.sword.y))

        game.screen.blit(self.font.render(u'PLACE', True, Colors.TITLE), (105, 349))
        game.screen.blit(self.font.render(game.locationtext, 6, Colors.WHITE), (200, 348))

        ###
        game.screen.blit(self.font.render(u'GOLD', True, Colors.TITLE), (105, 373))
        # game.screen.blit(self.font.render("%5s" % str(self.goldnumber), 6, Colors.WHITE), (190,372))
        game.screen.blit(self.font.render("%5s" % str('9999'), 6, Colors.WHITE), (190, 372))

        ###
        game.screen.blit(self.font.render(u'ALMAS', True, Colors.TITLE), (246, 373))
        # game.screen.blit(self.font.render("%17s" % str(self.almasnumber), 6, Colors.WHITE), (325, 373))
        game.screen.blit(self.font.render("%5s" % str('99990'), 6, Colors.WHITE), (325, 373))

    def drawlocationtext(self, text):
        # 사용하지 않는듯
        self.screen.blit(self.font.render(text, 6, Colors.WHITE), (200, 345))

    def setswordimage(self, imagefilename, r, g, b):
        self.swordimage = pygame.image.load(imagefilename).convert()
        self.swordimage.set_colorkey((r, g, b))
