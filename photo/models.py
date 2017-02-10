from django.db import models

# Create your models here.

class posts(models.Model): # A test for using models in the website
	title = models.CharField(max_length = 100)
	location = models.TextField()
	date = models.DateTimeField()
	# Failed but potentially could be useful