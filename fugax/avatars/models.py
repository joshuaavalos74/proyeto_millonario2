from django.db import models

# Create your models here.
class Avatar(models.Model):
	avatar = models.ImageField(upload_to = 'media/avatars')
	image = models.ForeignKey("avatars.Avatar", blank=True, null=True)
