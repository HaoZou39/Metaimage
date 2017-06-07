import os
import pyexiv2
filenames = next(os.walk('static\images'))[2]
print(filenames)
text = '12';
deletes =[];
for filename in filenames:
    metadata = pyexiv2.ImageMetadata('static\images\%s' %filename)
    metadata.read()
    tag = metadata['Exif.Image.ImageDescription']
    if text not in tag.raw_value:
        deletes.append(filename)
for delete in deletes:
    filenames.remove(delete)
print filenames
