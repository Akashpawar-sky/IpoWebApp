from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from IPO_App.views import IPOViewSet, ipo_list, ipo_details

# Set up the REST API router
router = DefaultRouter()
router.register(r'ipos', IPOViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # API endpoints for IPOViewSet
    path('', ipo_list, name='ipo_list'),  # Home page or IPO list
    path('ipo/<int:id>/', ipo_details, name='ipo_details'),  # IPO details
    path('upcoming-ipos/', ipo_list, name='upcoming_ipos'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
