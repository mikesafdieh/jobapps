#!/usr/bin/env python
import datetime
import os
import pytz
import sys

import django
from django.conf import settings

sys.path.insert(0, os.path.realpath(__file__ + '/../../'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "career_proj.settings")
django.setup()

from jobapps.models import JobApp


def main():
	create_intial_jobapps()


def create_intial_jobapps():
	JobApp.objects.get_or_create(
		title='Full Stack Software Engineer',
		company='Cockroach Labs',
		date_applied=datetime.datetime(2018, 10, 15, tzinfo=pytz.utc)
	)
	JobApp.objects.get_or_create(
		title='Full Stack Software Engineer',
		company='JW Player',
		date_applied=datetime.datetime(2018, 10, 16, tzinfo=pytz.utc)
	)
	JobApp.objects.get_or_create(
		title='Software Engineer',
		company='SeatGeek',
		date_applied=datetime.datetime(2018, 10, 18, tzinfo=pytz.utc)
	)
	JobApp.objects.get_or_create(
		title='Software Engineer',
		company='Foursquare',
		date_applied=datetime.datetime(2018, 10, 18, tzinfo=pytz.utc)
	)


if __name__ == '__main__':
	main()

