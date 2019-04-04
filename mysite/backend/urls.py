from django.urls import path

from . import views

urlpatterns = [
    path('testapi', views.testapi, name='testapi'),
    path('upload',views.upload, name='upload')
]