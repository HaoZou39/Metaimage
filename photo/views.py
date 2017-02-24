from django.shortcuts import render
import os 
from photo.models import posts
from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
import pyexiv2


def photo(request):
	filenames = next(os.walk('static\images'))[2]
	if(request.POST.get('submit')):
		text = request.POST.get('textinput');

	def submit(values,text):
		metadata = pyexiv2.ImageMetadata('static\images\%s' %values)
		metadata.read()
		key = 'Exif.Image.ImageDescription'
		metadata[key] = pyexiv2.ExifTag(key, text)
		metadata.write()
	
	if(request.POST.get('submit')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
				submit(values,text);
	return render(request,'index.html',{'filenames':filenames})