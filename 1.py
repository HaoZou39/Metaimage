import os
import sys
import pyexiv2

path = 'C:\Users\Hao Zou\Desktop\Metaimage\static\images'
dirs= os.listdir(path)
filenames = next(os.walk('static\images\Location'))[2]

for filename in filenames:
    print '--------------------------------------------------------------'
    metadata = pyexiv2.ImageMetadata('static\images\Location\%s' %filename)
    metadata.read()
    tag = metadata['Exif.GPSInfo.GPSLongitude']
    print(tag.raw_value)
