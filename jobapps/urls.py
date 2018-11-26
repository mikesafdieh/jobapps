from django.urls import path

from jobapps import views

# for namespacing (when dealing with multiple apps)
app_name = 'jobapps'

urlpatterns = [
	path('', views.index, name='index'),
	path('jobapps/', views.JobAppList.as_view(), name='jobapps_list'),
	path('jobapps/<int:pk>', views.JobAppDetail.as_view(), name='jobapps_detail'),
	# path('jobapps/', views.jobapps_list, name='jobapps_list'),
]