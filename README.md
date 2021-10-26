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
this program is in pre-alpha phase, and may not
even work if you download it and try it... More specifically, I think I have a bit
more work to do on Windows. On a POSIX platform, things seem to be running
smoothly enough.

To try out my take on Reverse-Engineering Geometry Dash [is it reverse
engineering?  I'm not sure... =) ], run GDtst.py in Python 2 or 3! (I checked
compatibility again recently...)
NOTE:  You need Pygame 2.0.0 or later installed!

Creating Levels:
I now have a working level editor, so use that. It may be a little buggy...
But I did what I could and it was waaaay faster than the previous method.

Program Structure:
Basically, I made a few classes.  One for the Cube sprite, including position,
cube frames, rotation and a few other things.  Then I made a class for
A) The Bricks in the level B) The spikes and other inanimate things that
hurt you C) The "bounceballs" (I can't think of a better name) D) The
BouncePads E) The Portals...  Then I made a Menu and GameLoop class to link
all the stuff I made together.  Also, I forgot to mention that there are a
few more classes that just fade into the background, and don't need to be tampered
with much.  1) BGeffects:  This draws some dark squares and circles in the
background, which move slowly and give a better arena scrolling feel.
2) PostProcessingEffects:  This can add some interesting effects.  I haven't
really developed it much, but it has a lot of potential.  Everything has to be done
by caching what's already onscreen, modifying it, and then pasting it back on the
screen.  3) FGeffects:  This is a class which lets you put moving shapes on
the screen which A) run for a certain number of frames B) can grow or shrink in size
over time C) can change color over time

What I want to add:
Controller support  
Optomisations that speed up my horrible code!  =)
Animated/motion capable blocks


Attribution to various people:
OXYGENE-1:  Jakob Fischer
            jakob@pizzadude.dk
            www.pizzadude.dk

PUSAB:  Ryoichi Tsunekawa
        http://flat-it.com/ (Flat-it)
        info@flat-it.com
