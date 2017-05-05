from django.db import models

class Perfil(models.Model):
	usuario=models.OneToOneField('auth.User')

class UserTag(models.Model):
	tag= models.ForeignKey('tags.Tag')
	user = models.ForeignKey('auth.User')

