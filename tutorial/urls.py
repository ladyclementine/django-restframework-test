from django.conf.urls import url, include
from rest_framework import routers
from quickstart import views
from quickstart.views import CotacaoRequestViewSet
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'SendCotacaoRequest', views.CotacaoRequestViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]