from django.conf.urls import url 
from main_app import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns=[
    url(r'^systemuser/$',views.systemuserApi),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)