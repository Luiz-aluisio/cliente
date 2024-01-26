
from django.urls import include,path
from rest_framework import routers
from cliente.core import views

router = routers.DefaultRouter()
router.register(r'cliente',views.ClienteViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
 ]

urlpatterns += router.urls

    


