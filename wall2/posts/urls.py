from django.urls import path, include

from posts import views
from posts.views import Entry
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'post', Entry)


urlpatterns = [
path('', include(router.urls)),
path('index', views.index, name='home'),
path('add/', views.add, name='add'),

]

