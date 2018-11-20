import datetime

from django.db import models
from django.utils import timezone


class JobApp(models.Model):
	title = models.CharField(max_length=200)
	company = models.CharField(max_length=200)
	description = models.TextField(default='', blank=True)
	date_applied = models.DateTimeField()

	def __str__(self):
		return f'{self.title}@{self.company}'
