from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('meetups/', views.index, name='all-meetups'),
  path('meetups/<slug:meetup_slug>/success', views.confirm_registration, name='confirm-registration'),
  path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup-detail'), # angle brackets for dynamic data, function in views to handle it
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)