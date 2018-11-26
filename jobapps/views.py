from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, renderers, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from jobapps.models import JobApp
from jobapps.serializers import JobAppSerializer


class JobAppList(generics.ListAPIView):
	queryset = JobApp.objects.all()
	serializer_class = JobAppSerializer

class JobAppDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = JobApp.objects.all()
	serializer_class = JobAppSerializer


def index(request):
	return HttpResponse('JopApps index :)')


