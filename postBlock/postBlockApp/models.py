from django.db import models

# Create your models here.

class blockPost(models.Model):

	title = models.CharField(max_length=250)
	text = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title