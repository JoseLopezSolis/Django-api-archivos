from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter() 

# /pdfapi
router.register('file', views.UserViewSet, basename='file')

urlpatterns = router.urls