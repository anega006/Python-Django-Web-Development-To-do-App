from django.db import models

# Create your models here.

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(auto_now=True, editable=False)

	def __str__(self):
		return self.item