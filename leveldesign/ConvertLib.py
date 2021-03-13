#Converter lib that takes human readable levels and turns them into Trigonometry Dash readable levels
#    Copyright (C) 2021  Lincoln V.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

# 1 = blocks 2 = triangles 3 & 0 = nothing 4 = bouncepad 5 = bounceball 6 = portal
def convert(level):
    blocks = []
    triangles = []
    bounceballs = []
    bouncepads = []
    portals = []
    for y in range(0,len(level)):
        for x in range(0,len(level[0])):
            if(level[y][x] == 2):
                try:
                    if(level[y + 1][x] == 1):
                        #triangle out == 1
                        triangles.append([y,x,1])
                    elif(level[y - 1][x] == 1):
                        #triangle out == 2
                        triangles.append([y,x,2])
                    elif(level[y][x + 1] == 1):
                        #triangle out == 4
                        triangles.append([y,x,4])
                    elif(level[y][x - 1] == 1):
                        #triangle out == 3
                        triangles.append([y,x,3])
                except IndexError:
                    triangles.append([y,x,1])
            elif(level[y][x] == 1):
                try:
                    if(level[y - 1][x] != 1 and level[y + 1][x] != 1):
                        #halfblock top
                        blocks.append([y,x,2])
                    else:
                        #wholeblock
                        blocks.append([y,x,1])
                except IndexError:
                    blocks.append([y,x,1])
            elif(level[y][x] == 4):
                #yellow bouncepad
                bouncepads.append([y,x,2])
            elif(level[y][x] == 5):
                #yellow bounceball
                bounceballs.append([y,x,2])
            elif(level[y][x] == 6):
                portals.append([y,x,1])

    #create a large empty list for the converted level (blocks)
    tmplist = []
    for x in range(0,len(level[0])):
        tmplist.append(0)
    outlistb = []
    for y in range(0,len(level)):
        outlistb.append(tmplist[:])
    del(tmplist)

     #create a large empty list for the converted level (triangles)
    tmplist = []
    for x in range(0,len(level[0])):
        tmplist.append(0)
    outlistt = []
    for y in range(0,len(level)):
        outlistt.append(tmplist[:])
    del(tmplist)

     #create a large empty list for the converted level (bouncepads)
    tmplist = []
    for x in range(0,len(level[0])):
        tmplist.append(0)
    outlistp = []
    for y in range(0,len(level)):
        outlistp.append(tmplist[:])
    del(tmplist)

     #create a large empty list for the converted level (bounceballs)
    tmplist = []
    for x in range(0,len(level[0])):
        tmplist.append(0)
    outlistl = []
    for y in range(0,len(level)):
        outlistl.append(tmplist[:])
    del(tmplist)

     #create a large empty list for the converted level (portals)
    tmplist = []
    for x in range(0,len(level[0])):
        tmplist.append(0)
    outlists = []
    for y in range(0,len(level)):
        outlists.append(tmplist[:])
    del(tmplist)

    #clone the list created above for each type of GD block
    blocksout = outlistb[:]
    trianglesout = outlistt[:]
    bounceballsout = outlistl[:]
    bouncepadsout = outlistp[:]
    portalsout = outlists[:]

    #add in the various GD blocks to game lists
    for z in range(0,len(blocks)):
        blocksout[blocks[z][0]][blocks[z][1]] = blocks[z][2]
    for x in range(0,len(triangles)):
        trianglesout[triangles[x][0]][triangles[x][1]] = triangles[x][2]
    for x in range(0,len(bounceballs)):
        bounceballsout[bounceballs[x][0]][bounceballs[x][1]] = bounceballs[x][2]
    for x in range(0,len(bouncepads)):
        bouncepadsout[bouncepads[x][0]][bouncepads[x][1]] = bouncepads[x][2]
    for x in range(0,len(portals)):
        portalsout[portalsout[x][0]][portalsout[x][1]] = portals[x][2]

    #return output
    return [blocksout,trianglesout,bouncepadsout,bounceballsout,portalsout]
