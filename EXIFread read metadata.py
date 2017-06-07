import os
import sys
import exifread

path = 'C:\Users\Hao Zou\Desktop\Metaimage\static\images'

dirs= os.listdir(path)
for file in dirs:
    print 'file:' + os.path.join(path,file)
    print '--------------------------------------------------------------'

    f = open(os.path.join(path,file), 'rb')
    tags = exifread.process_file(f)
    for selected_tag in tags.keys():
        if selected_tag in (
        'EXIF UserComment','Image ImageDescription'):
            print "Selected Keys: %s:    %s" % (selected_tag, tags[selected_tag])
    print '--------------------------------------------------------------'
