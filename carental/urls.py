from .views import accueil, car_list
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Car/', include('Car.urls')),
    path('CarModel/', include('CarModel.urls')),
    path('CarMark/', include('CarMark.urls')),
    path('', accueil, name='accueil'),
    path('accounts/login/', LoginView.as_view(), name='login'),  # Configuration de l'URL de connexion
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
