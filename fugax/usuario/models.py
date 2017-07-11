from django.db import models

class Perfil(models.Model):
	usuario=models.OneToOneField('auth.User')
	imagen = models.ImageField(null=True)

	def __str__(self):
		return str(self.usuario)

class UserTag(models.Model):
	tag= models.ForeignKey('tags.Tag')
	user = models.ForeignKey('auth.User')

