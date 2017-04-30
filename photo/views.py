from django.shortcuts import render
import os 
from photo.models import posts
from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
import pyexiv2
import csv
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import ctypes  # An included library with Python install.

def photo(request):
	filenames = next(os.walk('static\images'))[2]
	deletes =[];
	keytext='';
	lats =[];
	lat = [];
	log = [];
	logs =[];
	values=''
	latlogs=[];
	if(request.GET.get('submit')):
		text = request.GET.get('textinput');
	if(request.GET.get('Imagedescrip')):
		keytext = request.GET.get('searchtext');
	if(request.GET.get('Usercomment')):
		keytext = request.GET.get('searchtext');	 
	if(request.GET.get('CSV')):
		with open('example.csv', 'rb') as f:
			reader = csv.reader(f);
			list1 = list(reader);
			text = ','.join([str(i) for i in list1])
			
	def submit(values,text):
		metadata = pyexiv2.ImageMetadata('static\images\%s' %values)
		metadata.read()
		key = 'Exif.Image.ImageDescription'
		metadata[key] = pyexiv2.ExifTag(key, text)
		metadata.write()
			
	def CSVchange(values,text):
		metadata = pyexiv2.ImageMetadata('static\images\%s' %values)
		metadata.read()
		key = 'Exif.Photo.UserComment'
		metadata[key] = pyexiv2.ExifTag(key, text)
		metadata.write()
		
	def imagedescript(filenames,keytext):
		for filename in filenames:
			metadata = pyexiv2.ImageMetadata('static\images\%s' %filename)
			metadata.read()
			tag = metadata['Exif.Image.ImageDescription'];
			if keytext not in tag.raw_value:
				deletes.append(filename)
		for delete in deletes:
			filenames.remove(delete)
		return filenames;
	
	def usercomment(filenames,keytext):
		for filename in filenames:
			metadata = pyexiv2.ImageMetadata('static\images\%s' %filename)
			metadata.read()
			tag = metadata['Exif.Photo.UserComment'];
			if keytext not in tag.raw_value:
				deletes.append(filename)
		for delete in deletes:
			filenames.remove(delete)
		return filenames;	
	
	def get_exif_data(image):
		"""Returns a dictionary from the exif data of an PIL Image item. Also converts the GPS Tags"""
		exif_data = {}
		info = image._getexif()
		if info:
			for tag, value in info.items():
				decoded = TAGS.get(tag, tag)
				if decoded == "GPSInfo":
					gps_data = {}
					for t in value:
						sub_decoded = GPSTAGS.get(t, t)
						gps_data[sub_decoded] = value[t]

					exif_data[decoded] = gps_data
				else:
					exif_data[decoded] = value

		return exif_data

	def _get_if_exist(data, key):
		if key in data:
			return data[key]
		
		return None 
	
	def _convert_to_degress(value):
		"""Helper function to convert the GPS coordinates stored in the EXIF to degress in float format"""
		d0 = value[0][0]
		d1 = value[0][1]
		d = float(d0) / float(d1)

		m0 = value[1][0]
		m1 = value[1][1]
		m = float(m0) / float(m1)

		s0 = value[2][0]
		s1 = value[2][1]
		s = float(s0) / float(s1)

		return d + (m / 60.0) + (s / 3600.0)

	def get_lat_lon(exif_data):
		"""Returns the latitude and longitude, if available, from the provided exif_data (obtained through get_exif_data above)"""
		lat = None
		lon = None
		if "GPSInfo" in exif_data:		
			gps_info = exif_data["GPSInfo"]
			gps_latitude = _get_if_exist(gps_info, "GPSLatitude")
			gps_latitude_ref = _get_if_exist(gps_info, 'GPSLatitudeRef')
			gps_longitude = _get_if_exist(gps_info, 'GPSLongitude')
			gps_longitude_ref = _get_if_exist(gps_info, 'GPSLongitudeRef')
			if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
				lat = _convert_to_degress(gps_latitude)
				if gps_latitude_ref != "N":                     
					lat = 0 - lat
				lon = _convert_to_degress(gps_longitude)
				if gps_longitude_ref != "E":
					lon = 0 - lon
		return lat, lon	
	
	if(request.GET.get('submit')):
		for checkbox in filenames:
			values = request.GET.get(checkbox);
			if values != None:
				submit(values,text);
				
	if(request.GET.get('CSV')):
		for checkbox in filenames:
			values = request.GET.get(checkbox);
			if values != None:
				CSVchange(values,text);
	
	if(request.GET.get('GPS')):
		for checkbox in filenames:
			values = request.GET.get(checkbox);
			if values != None:
				image = Image.open('static\images\%s'%values)
				exif_data = get_exif_data(image)
				[lat,log] = get_lat_lon(exif_data);			
				lats.append(lat);
				logs.append(log);
		latlogs = zip(lats,logs);
				
	if(request.GET.get('Imagedescrip')):
		imagedescript(filenames,keytext);		
	if(request.GET.get('Usercomment')):	
		usercomment(filenames,keytext);
		
	return render(request,'index.html',{'filenames':filenames,'keytext':keytext,'lats':lats,'logs':logs,'values':values,'latlogs':latlogs})