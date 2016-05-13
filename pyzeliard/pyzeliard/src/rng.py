
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


###
### NOTE : weapons also have a dexterity built-in !
###


import pygame
from pygame.locals import *
from random import *

class RNG:
    "Random Number God"
    def __init__(self, gameobj):
        self.gameobj = gameobj

    def rolld400(self):
        return randint(1,400)

    def rolld200(self):
        return randint(1,200)

    def rolld100(self):
        return randint(1,100)

    def rolld50(self):
        return randint(1,50)

    def rolld40(self):
        return randint(1,40)

    def rolld30(self):
        return randint(1,30)

    def rolld20(self):
        return randint(1,20)

    def rolld10(self):
        return randint(1,10)

    def rolld7(self):
        return randint(1,7)

    def rolld6(self):
        return randint(1,6)

    def rolld5(self):
        return randint(1,5)

    def rolld4(self):
        return randint(1,4)

    def rolld3(self):
        return randint(1,3)

    def rolld2(self):
        return randint(1,2)

    def rollbetween(self, min, max):
        return randint(min,max)

    def rollplayersword(self,player):
        if randint(0,3) > 2:
            return 0

        r = player.swordroll() 
        if r == 4: # critical hit
            return 4*2
        else:
            return r

    def rollbroadsword(self):
        if randint(0,3) > 2:
            return 0
        
        r = self.rolld4()
        if r == 4: # critical hit
            return 4*2
        else:
            return r

    def rolllongbow(self):
        if randint(0,20) > self.gameobj.dexterity.get():
            return 0
        
        r = self.rolld8()
        if r == 4: # critical hit
            return 8*2
        else:
            return r

    def rollbow(self):
        if randint(0,20) > self.gameobj.dexterity.get():
            return 0
        
        r = self.rolld4()
        return r

    def rollvampirictouch1(self):
        return self.rolld4() + 3

    def rollshockinggrasp1(self):
        return self.rolld4() + 0

    def rollmagicmissile1(self):
        return self.rolld2() + 0

    def rollmagicmissile2(self):
        return self.rolld4() + 1 

    def rollmagicmissile3(self):
        return self.rolld4() + 3

    def rollfireball1(self):
	return self.rolld6() + 2

    def rollfireball2(self):
	return self.rolld7()

    def rollfireball3(self):
	return self.rolld7() + 3

    def rollghostwithlantern(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld2()
        return r

    def rollfishman(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld2()
        return r

    def rollcavebat1(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld2()
        return r

    def rollhobgoblin(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld5()
        return r

    def rollgoblinknife(self):
        if self.rolld20() > self.gameobj.dexterity.get() or self.gameobj.agility.get() % self.rolld20() <= 2:
            return 0

	if self.gameobj.luck.get() % self.rolld50() <= 2:
	    return 0
        
        r = self.rolld2() + self.gameobj.strength.get() % 2
        return r

    def rollvenomspit(self):
        if randint(0,1) <= 0:
            return 0
        
        r = self.rolld6()
        return r

    def rollknife(self):
        if randint(0,20) > self.gameobj.dexterity.get():
            return 0
        
        r = self.rolld2() + self.gameobj.strength.get() % 2
        return r

    def rollthrowknife(self):
        if randint(0,20) > self.gameobj.dexterity.get() and self.gameobj.throwing.get() % 100 <= self.rolld100() + 50:
            return 0
	if self.rolld4() == 1:
		if self.gameobj.luck.get() % 100 >= 1:
			return 0

	if self.gameobj.agility.get() % self.rolld40() <= 2:
		return 0
        
        r = self.rolld2() + self.gameobj.strength.get() % 2
        return r

    def rollbullfrog(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld2()
        return r

    def rollknight(self):
        if randint(0,30) <= 28:
            return 0
        
        r = self.rolld6()
        return r

    def rollspider(self):
        if self.rolld20() > self.gameobj.dexterity.get():
            return 0
        
        r = self.rolld2() % self.rolld2()
        return r

    def rollskeleton(self):
        if self.rolld20() > self.gameobj.dexterity.get():
            return 0
        
        r = self.rolld2()
        return r

    def rollscorpionred(self):
        if randint(0,3) <= 2:
            return 0
        
        r = self.rolld2()
        return r
   
    def rollbeholderbatzap(self):
	if randint(0,4) <= 3:
		return 0

	r = self.rolld2()
	return r

    def rolloverseerbeholder(self):
	if self.rolld20() > self.gameobj.dexterity.get(): 
		return 0

	r = self.gameobj.strength.get() - self.rolld5()
	return r

    def rollgauthbeholder(self):
	if self.rolld20() > self.gameobj.dexterity.get() or self.gameobj.agility.get() % self.rolld20() <= 1: 
		return 0

	if self.rolld2() == 1:
		if self.gameobj.luck.get() % self.rolld20() <= 1:
			return 0

	r = self.gameobj.strength.get() - self.rolld5()
	return r

    def rollbeholder(self):
	if self.rolld20() > self.gameobj.dexterity.get(): 
		return 0

	r = self.gameobj.strength.get() - self.rolld4()
	return r

    def rollabeille1(self):
	if randint(0,1) == 0:
		return 0

	r = self.rolld2()
	return r

    def rollabeillequeen(self):
	if randint(0,10) == 0:
		return 0

	r = self.rolld2()
	return r
