from django.shortcuts import render
import os 
from photo.models import posts
# Create your views here.
from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
#from PIL import Image
#from PIL.ExifTags import TAGS
#import pyexiv2

def photo(request):
	post = posts.objects.all()
#	dir = os.path.dirname(__file__)
#	filepath = os.path.join(dir, '..\static\images')
#	filenames = paths[50:]
#	filenames = next(os.walk(filepath))[2]
	filenames = ['DSC_0059.JPG', 'Duzce-12-18 and 19-99_078.jpg', 'Duzce-12-18 and 19-99_079.jpg', 'Duzce-12-18 and 19-99_080.jpg', 'Duzce-12-18 and 19-99_088.jpg']
	if(request.POST.get('submit')):
		text = request.POST.get('textinput');

	def submit(values,text):

		img = Image.open('../static/images/%s' %values)
		img.save('../../Downloads/%s' %values)
#		metadata = pyexiv2.ImageMetadata('C:/Users/Hao Zou/Downloads/%s' %values)
#		metadata.read()
#		key = 'Exif.Image.ImageDescription'
#		metadata[key] = pyexiv2.ExifTag(key, text)
#		metadata.write()
#		img = pexif.JpegFile.fromFile('d:/DSC_0059.JPG')


	if(request.POST.get('submit')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
				submit(values,text);
	return render(request,'index.html',{'filenames':filenames})