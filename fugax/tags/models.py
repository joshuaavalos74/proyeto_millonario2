from django.db import models

# Create your models here.
class Tag(models.Model):
	name = models.CharField(max_length=40)
	parent_tag= models.ForeignKey("tags.Tag", blank=True, null=True)	

	def __str__(self):
		return "%s" %(self.nombre)