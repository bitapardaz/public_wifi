from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)
	confirmed = models.BooleanField(default = False)
	thumbnail = models.ImageField(upload_to='images',null=True,max_length=300)
	image = models.ImageField(upload_to='images',null=True,max_length=300)
	date_published = models.DateTimeField(auto_now=True,editable=True)

	def __unicode__(self):
		return self.name

class ParticipantType(models.Model):
	title = models.CharField(max_length=200)

class Participant(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images',null=True,max_length=300)


class Movie(models.Model):

	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images',null=True,max_length=300)
	wide_image = models.ImageField(upload_to='images',null=True,max_length=300)
	confirmed = models.BooleanField(default=False)
	price = models.IntegerField(default =0)
	category = models.ForeignKey(Category)
	date_published = models.DateTimeField(auto_now=True,editable=True)
	file_path = models.FilePathField(path="/mnt/FlashDrive/wifi_storage/movies/",allow_folders=False,null=True,blank=True)
	description = models.CharField(max_length=1000,null=True,blank=True)
	order = models.IntegerField(default=0)


class MovieParticipant(models.Model):
	movie = models.ForeignKey(Movie)
	participant = models.ForeignKey(Participant)
	ParticipantType = models.ForeignKey(ParticipantType)
