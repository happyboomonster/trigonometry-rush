import pickle

#change the name of this file:  it's what we will be pickling.
#you can take the output from out.levelconv and shove it directly in here.
infilename = "BackOnTrack/out.levelconv"

#this is the file that the pickled data gets stored into.
#a list is how it's done, with several sublists:
#squares map, triangles, bouncepads, bounceballs, and portals, in that order.
outfilename = "BackOnTrack/OutputLevel.pkl"

infile = open(infilename, "r")
newfile = open(outfilename,"w")

#good function we need in a little
def getlist(infile):
    NotSpace = True
    returnstring = "["
    while NotSpace:
        tmp = infile.readline()
        if(tmp == ""):
            returnstring = returnstring + "]"
            NotSpace = False
        elif(list(tmp)[0] == "T"):
            infile.seek(-40,1)
            returnstring = returnstring + "]"
            NotSpace = False
        else:
            returnstring = returnstring + tmp + "\n"
    return returnstring

#now we take the data from IN, and turn it into some python2/3 understandable
#lists for OUTPUT.
string = ""
string = string + "["
run = True
while run:
    tmp = infile.readline()
    if(tmp == ""):
        run = False
    else:
        if(list(tmp)[0] == "T"):
            MapType = list(tmp)[10] + list(tmp)[11] + list(tmp)[12] + list(tmp)[13] + list(tmp)[14] + list(tmp)[15] + list(tmp)[16]
            if(MapType == "BounceB"):
                string = string + getlist(infile) + ","
            elif(MapType == "BounceP"):
                string = string + getlist(infile) + ","
            elif(MapType == "Squares"):
                string = string + getlist(infile) + ","
            elif(MapType == "Triangl"):
                string = string + getlist(infile) + ","
            elif(MapType == "Portals"):
                string = string + getlist(infile) + "]"

exec("level = " + string)
pickle.dump(level, newfile)

newfile.close()
infile.close()
