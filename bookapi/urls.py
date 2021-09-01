from django.urls import include, path
from rest_framework import routers
from .views import BooksViewSet, dbViewSet

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'db', dbViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('get_data/', BooksViewSet.get_data),

]