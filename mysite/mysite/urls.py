from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.views.generic.base import TemplateView


urlpatterns = [
    # url(r'^admin/',admin.site.urls),
    # url(r'', TemplateView.as_view(template_name='index.html')),
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="index.html")),
    path('api/', include('backend.urls')),
]
