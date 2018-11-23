from rest_framework import serializers

from .models import JobApp


class JobAppSerializer(serializers.ModelSerializer):

	class Meta:
		model = JobApp
		fields = ('title', 'company', 'description', 'date_applied',)

