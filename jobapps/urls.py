from django.urls import path

from . import views

# for namespacing (when dealing with multiple apps)
app_name = 'jobapps'

urlpatterns = [
	path('', views.index, name='index'),
]