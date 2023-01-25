
from django.contrib import admin
from django.urls import path
from dbjob import views
from dbjob.views import FormCreate
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('geography', views.geography, name='geography'),
    path('skills', views.skills, name='skills'),
    path('lastVacancies', FormCreate.as_view(), name='lvacancies'),
    path('demand', views.demand, name='demand'),
    path('error', views.error, name='error'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)