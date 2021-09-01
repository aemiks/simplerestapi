from django.urls import include, path
from rest_framework import routers
from .views import BooksViewSet

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('db/', BooksViewSet.get_data),

]