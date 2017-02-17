import os
rootDir = "../static/images"
fileSet = set()

for dir_, _, files in os.walk(rootDir):
    for fileName in files:
        relDir = os.path.relpath(dir_, rootDir)
        relFile = os.path.join(relDir, fileName)
        fileSet.add(relFile)
print fileSet

filenames = next(os.walk('../static/images'))[2]
print filenames
