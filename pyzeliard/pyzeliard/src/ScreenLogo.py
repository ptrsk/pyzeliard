#-*- coding: cp949 -*-
#�Ϸ���

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

from time import *
from Screen import *

class ScreenLogoC:
    
    def __init__(self,screen):
        
        print("display_height->")
        
        display_height= screen.display_height
        print(display_height)
        
        pygame.font.init()
        
        
        fontName = "Courier"
        fontColor = (255,255,255)# RGB
        fontBold = True #����
        #fontItalic = True #�����
        fontItalic= False
        fontSize= 20  #��Ʈ ũ��
        offset_height=100   #��Ʈ ����

        text1= "Copyright (C)1987,1990 GAME ARTS"
        text2= "Copyright (C)1990 Sierra On-Line"
        text3= 'Copyright (C)2015 GPL Project'
        
        
        x=60 #�� 60������ �´�
        y= display_height-offset_height # ��Ʈ�� ���� ����
        fontObj = pygame.font.SysFont(fontName, fontSize, fontBold, fontItalic) 
        textSurfaceObj = fontObj.render(text1, fontBold, fontColor)   # �ؽ�Ʈ ��ü�� �����Ѵ�. ù��° �Ķ���ʹ� �ؽ�Ʈ ����, �ι�°�� Anti-aliasing ��� ����, ����°�� �ؽ�Ʈ �÷��� ��Ÿ����
        #textRectObj = textSurfaceObj.get_rect() # �ؽ�Ʈ ��ü�� ��� ��ġ�� �����´�
        textRectObj = (x, y)                                 # �ؽ�Ʈ ��ü�� ��� �߽� ��ǥ�� �����Ѵ�
        screen.blit(textSurfaceObj, textRectObj)                      # ������ ��ġ�� �ؽ�Ʈ ��ü�� ����Ѵ�
        #self.createText(text1, fontName, fontBold, fontItalic, fontColor, fontSize, x, y)
        
        y = display_height-offset_height+(fontSize*1)
        fontObj = pygame.font.SysFont(fontName, fontSize, fontBold, fontItalic) 
        textSurfaceObj = fontObj.render(text2, fontBold, fontColor)
        #textRectObj = textSurfaceObj.get_rect()
        textRectObj = (x, y)
        screen.blit(textSurfaceObj, textRectObj)
        

        y=display_height-offset_height+(fontSize*2)
        fontObj = pygame.font.SysFont(fontName, fontSize, fontBold, fontItalic) 
        textSurfaceObj = fontObj.render(text3, fontBold, fontColor)
        #textRectObj = textSurfaceObj.get_rect()
        textRectObj = (x, y)
        screen.blit(textSurfaceObj, textRectObj)
        
#
        image = pygame.image.load('./pics/image 7.png').convert()
       
        gameover = 0
        while gameover == 0:
            pygame.display.update()
            
            #ToDo:�̹����� �Ⱥ����ٱ� ���̵� �� �Ǿ����
            self.blit(image, (display_width*0.1, 10))
            sleep(0.01)
            for event in pygame.event.get():
                # �������� �ݱ� ��ư�� ������ ��, ���α׷��� �����ϵ��� ó��
                if event.type == QUIT:
                    print("������ ���� ���� ��û")
                    sys.exit()
                    
                
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1
                    
    # text, Font Name, size,  fontBold, fontItalic
    # ToDo: function has a problem                     
    def createText(text, fontName, fontBold, fontItalic, fontColor, fontSize, x, y):
        fontObj = pygame.font.SysFont(fontName, fontSize, fontBold, fontItalic) 
        textSurfaceObj = fontObj.render(text1, fontBold, fontColor)   # �ؽ�Ʈ ��ü�� �����Ѵ�. ù��° �Ķ���ʹ� �ؽ�Ʈ ����, �ι�°�� Anti-aliasing ��� ����, ����°�� �ؽ�Ʈ �÷��� ��Ÿ����
        textRectObj = textSurfaceObj.get_rect()              # �ؽ�Ʈ ��ü�� ��� ��ġ�� �����´�
        textRectObj = (x, y)                                 # �ؽ�Ʈ ��ü�� ��� �߽� ��ǥ�� �����Ѵ�
        self.blit(textSurfaceObj, textRectObj)                      # ������ ��ġ�� �ؽ�Ʈ ��ü�� ����Ѵ�
        
        return 1
