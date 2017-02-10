# Libraries Used for this project
from django.shortcuts import render
from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
import os # Library used to read files in one folder
from photo.models import posts
import ctypes #Library for pop up window
import pyexiv2 #Library used for metadata
from shutil import copyfile # Library used to copy files
# Create your views here.

def photo(request):
	post = posts.objects.all()
	filenames = next(os.walk('C:/Users/Hao Zou/Metaimage/static/images'))[2] # Acquire filenames for all files under a certain folder
	# Acquire text input once change button is clicked
	if(request.POST.get('change')):
		text = request.POST.get('textinput');
	# Acquire text input once append button is clicked
	if(request.POST.get('append')):
		text = request.POST.get('textinput');
	# Acquire text input once chan button is clicked
	if(request.POST.get('chan')):
		newname = request.POST.get('filename');
	# Acquire text input once copy button is clicked
	if(request.POST.get('copy')):
		newname = request.POST.get('filename');
	# Sort the filenames from A to Z once sort1 button is clicked
	if(request.POST.get('sort1')):
		filenames = list(reversed(filenames));
		filenames = list(reversed(filenames));
	# Sort the filenames from Z to A once sort button is clicked
	if(request.POST.get('sort')):
		filenames = list(reversed(filenames));
	#Function for changing metadata of photos	
	def change(values,text):
		temp = Image.open('C:/Users/Hao Zou/Metaimage/static/images/%s' %values) # Open a temperate file
		temp.save('C:/Users/Hao Zou/Metaimage/static/%s' %values) # Save that temperate file in another folder
		# Change the metadata by first read it and then write it into certain key
		metadata = pyexiv2.ImageMetadata('C:/Users/Hao Zou/Metaimage/static/%s' %values) 
		metadata.read()
		key = 'Exif.Image.ImageDescription' # The key or the tag name of the specific metadata
		metadata[key] = pyexiv2.ExifTag(key, text)
		metadata.write() # Write in the changes of the metadata
		copyfile('C:/Users/Hao Zou/Metaimage/static/%s' %values,'C:/Users/Hao Zou/Downloads/%s' %values) # Download the temperate file into users' device
		os.remove('C:/Users/Hao Zou/Metaimage/static/%s' %values) # delete the temperate file
#		img = pexif.JpegFile.fromFile('d:/DSC_0059.JPG')

	#Function for adding metadata into existing metadata of photos	
	def append(values,text):
			copyfile('C:/Users/Hao Zou/Metaimage/static/images/%s' %values,'C:/Users/Hao Zou/Metaimage/static/%s' %values)# Copy the file to make a temperate file
			# Read the exsisting metadata first
			metadata = pyexiv2.ImageMetadata('C:/Users/Hao Zou/Metaimage/static/images/%s' %values)
			metadata.read()
			key = 'Exif.Image.ImageDescription'
			tag = metadata['Exif.Image.ImageDescription']
			final = text + tag.value # Adding exsisting metadata with new metadata to make a new string 
			metadata[key] = pyexiv2.ExifTag(key, final)
			metadata.write() # Write in the sum of the metadata
			copyfile('C:/Users/Hao Zou/Metaimage/static/%s' %values,'C:/Users/Hao Zou/Downloads/%s' %values)# Download the temperate file into users' device
			os.remove('C:/Users/Hao Zou/Metaimage/static/%s' %values) # delete the temperate file

	#Function used to append the filename of photos		
	def chan(values,newname):
		temp = Image.open('C:/Users/Hao Zou/Metaimage/static/images/%s' %values)# Open a temperate file
		name = newname+values # Make a new string by adding the append with the original filename 
		temp.save('C:/Users/Hao Zou/Metaimage/static/images/%s' %name) # save the new filename
		os.remove('C:/Users/Hao Zou/Metaimage/static/images/%s' %values)# delete the original file

	#Function used to append the filename of photos and download it without changing the original file
	def copy(values,newname):
		name = newname+values # Create a new string of combined filename
		copyfile('C:/Users/Hao Zou/Metaimage/static/images/%s' %values,'C:/Users/Hao Zou/Downloads/%s' %name) # Download the new file with new filename without changing the original file

	# Calling the function change
	if(request.POST.get('change')):
		for checkbox in filenames:       # Use for loop to go through all the chosen files
			values = request.POST.get(checkbox);
			if values != None:
				change(values,text);

	# Calling the function append				
	if(request.POST.get('append')):
		for checkbox in filenames:       # Use for loop to go through all the chosen files
			values = request.POST.get(checkbox);
			if values != None:
				append(values,text);
	
	# Calling the function chan	
	if(request.POST.get('chan')):
		for checkbox in filenames:       # Use for loop to go through all the chosen files
			values = request.POST.get(checkbox);
			if values != None:
				chan(values,newname);
	
	# Calling the function copy
	if(request.POST.get('copy')):
		for checkbox in filenames:       # Use for loop to go through all the chosen files
			values = request.POST.get(checkbox);
			if values != None:
				copy(values,newname);
	
	return render(request,'index.html',{'filenames':filenames}) # return to the website, passing the variable: filenames