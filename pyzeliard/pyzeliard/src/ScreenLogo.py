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
        fontBold = True #굵게
        #fontItalic = True #기울임
        fontItalic= False
        fontSize= 20  #폰트 크기
        offset_height=100   #폰트 간격

        text1= "Copyright (C)1987,1990 GAME ARTS"
        text2= "Copyright (C)1990 Sierra On-Line"
        text3= 'Copyright (C)2015 GPL Project'
        
        
        x=60 #약 60정도가 맞다
        y= display_height-offset_height # 폰트의 높이 조정
        fontObj = pygame.font.SysFont(fontName, fontSize, fontBold, fontItalic) 
        textSurfaceObj = fontObj.render(text1, fontBold, fontColor)   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
        #textRectObj = textSurfaceObj.get_rect() # 텍스트 객체의 출력 위치를 가져온다
        textRectObj = (x, y)                                 # 텍스트 객체의 출력 중심 좌표를 설정한다
        screen.blit(textSurfaceObj, textRectObj)                      # 설정한 위치에 텍스트 객체를 출력한다
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
            
            #ToDo:이미지가 안보였다기 페이드 인 되어야함
            self.blit(image, (display_width*0.1, 10))
            sleep(0.01)
            for event in pygame.event.get():
                # 윈도우의 닫기 버튼이 눌렸을 때, 프로그램을 종료하도록 처리
                if event.type == QUIT:
                    print("윈도우 강제 종료 요청")
                    sys.exit()
                    
                
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1
                    
    # text, Font Name, size,  fontBold, fontItalic
    # ToDo: function has a problem                     
    def createText(text, fontName, fontBold, fontItalic, fontColor, fontSize, x, y):
        fontObj = pygame.font.SysFont(fontName, fontSize, fontBold, fontItalic) 
        textSurfaceObj = fontObj.render(text1, fontBold, fontColor)   # 텍스트 객체를 생성한다. 첫번째 파라미터는 텍스트 내용, 두번째는 Anti-aliasing 사용 여부, 세번째는 텍스트 컬러를 나타낸다
        textRectObj = textSurfaceObj.get_rect()              # 텍스트 객체의 출력 위치를 가져온다
        textRectObj = (x, y)                                 # 텍스트 객체의 출력 중심 좌표를 설정한다
        self.blit(textSurfaceObj, textRectObj)                      # 설정한 위치에 텍스트 객체를 출력한다
        
        return 1
