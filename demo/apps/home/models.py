from django.db import models
from django.contrib.auth.models import User



class userProfile(models.Model):
	
	def url(self,filename):
		ruta = "MultimediaData/Users/%s/%s"%(self.user.username,filename)
		return ruta


	user 		=	models.OneToOneField(User)
	photo 		=	models.ImageField(upload_to=url)
	telefono	=	models.CharField(max_length=30)

	def __unicode__(self):
		return self.user.username