This is a newer directory.  In here, I hope to place all levels which the game should be capable of running.
Automatically, the game should make note of all the folders and their names in here.  Then, it will unpickle
a level file inside that folder, and use that as the level.  Here's how the pickle file should be stored:

picklefile([SquaresCourse,TrianglesCourse,BouncePadsCourse,BounceBallsCourse,PortalsCourse])]

You make a folder with the title of your level (no spaces) as the folder name, and place the
out.levelconv file in there.  Then modify Pickler.py so that "infilename" equals
"[your level folder]/out.levelconv".  Change "outfilename" so that it equals "[your level folder]/
[the name you want your pickle file to be]".

Making the game recognize these pickle files will be harder, and I haven't implemented this yet.
I suggest you end your level pickles with the file ending ".pkl" to make it easier to standardize
and implement this later on.
