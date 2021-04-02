import pickle

#due to the way pickle works in python 2 vs. 3, I have to check
#if the user is using python 2 or 3 via a error giving script
# - but only gives an error in python 3!
try:
    mifile = open("TestLevel01/OutputLevel.pkl","r")
    pickle.load(mifile)
    PYTHON2 = True
    PYTHON3 = False
    print("You're using Python 2. Continuing...")
except TypeError:
    PYTHON2 = False
    PYTHON3 = True
    print("You're using Python 3. Continuing...")

#change the name of this file:  it's what we will be pickling.
#you can take the output from out.levelconv and shove it directly in here.
infilename = "BackOnTrack/out.levelconv"

#this is the file that the pickled data gets stored into.
#a list is how it's done, with several sublists:
#squares map, triangles, bouncepads, bounceballs, and portals, in that order.
#you're supposed to change this to your filename you want your level stored in.
outfilename = "BackOnTrack/OutputLevel.pkl"

if(PYTHON2):
    newfile = open(outfilename,"w")
    infile = open(infilename, "r")
elif(PYTHON3):
    newfile = open(outfilename,"wb")
    infile = open(infilename, "rb")

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
            if(PYTHON2):
                infile.seek(-40,1)
            elif(PYTHON3):
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
if(PYTHON2):
    pickle.dump(level, newfile)
elif(PYTHON3):
    pickle.dump(level,newfile,2)

newfile.close()
infile.close()
