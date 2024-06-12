from django.urls import path
from .views import HomeView,LogoutView
from django.conf import settings
from django.conf.urls.static import static

app_name = "website"

urlpatterns = [
    path('home/',HomeView.as_view(),name="home"),
    path('logout/',LogoutView.as_view(),name="logout"),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

