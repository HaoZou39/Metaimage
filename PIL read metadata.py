from PIL import Image
from PIL.ExifTags import TAGS
import os
import sys

path = 'C:\Users\Hao Zou\Desktop\Sample_images\BIBE'
dirs= os.listdir(path)
for file in dirs:
    print 'file:' + os.path.join(path,file)
    print '--------------------------------------------------------------'
    for (k,v) in Image.open(os.path.join(path,file))._getexif().iteritems():
 #       if TAGS.get(k) == 'UserComment':
                print '%s = %s' % (TAGS.get(k), v)
