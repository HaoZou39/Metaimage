import os

dir = os.path.dirname(__file__)
filepath = os.path.join(dir, '..\static\images')
#	filenames = paths[50:]
filenames = next(os.walk(filepath))[2]
print filenames
