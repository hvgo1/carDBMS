from __future__ import unicode_literals

from django.db import models

class Car(models.Model):
	color = models.CharField(max_length=20)
	position = models.IntegerField()

	def __str__(self):
		return self.color
