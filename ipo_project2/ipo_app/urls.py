from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, IPOViewSet, DocumentViewSet, ipo_list_view

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'ipos', IPOViewSet)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('', ipo_list_view, name='ipo-list'),
    path('api/', include(router.urls)),
]
