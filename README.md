README
Copyright (C) 2021  Lincoln V.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Hopefully this README is helpful...  First of all, I want to mention that
this program is in pre-alpha phase (like really pre-alpha), and may not
even work if you download it and try it...

To try out my take on Reverse-Engineering Geometry Dash [is it reverse
engineering?  I'm not sure... =) ], run GDtst.py in Python 2 or 3! (Actually,
Python 3 for the moment doesn't work due to some...problems with Pickle)
(both should work fine, although I don't actively use Python 3 so there
 might be some bugs...)  NOTE:  You need Pygame 2 or later installed!

Creating Levels:
Please refer to the README in the "leveldesign" folder.  More to come in
a little?

Program Structure:
Basically, I made a few classes.  One for the Cube sprite, including position,
cube frames, rotation and a few other things.  Then I made a class for
A) The Bricks in the level B) The spikes and other inanimate things that
hurt you C) The "bounceballs" (I can't think of a better name) D) The
BouncePads E) The Portals...  Then I made a Menu and GameLoop class to link
all the stuff I made together.

What I want to add:  Changeable cube costumes, and a menu for that.  
A front menu [WHAT, I know...  I don't have a front menu yet  =(  ].  
Controller and custom control setup support.  
Optomisations that speed up my horrible code!  =) .  
Make it easier for people to make levels.  


Attribution to various people:
OXYGENE-1:  Jakob Fischer
            jakob@pizzadude.dk
            www.pizzadude.dk

PUSAB:  Ryoichi Tsunekawa
        http://flat-it.com/ (Flat-it)
        info@flat-it.com
