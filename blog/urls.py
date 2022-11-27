from django.urls import path
from .views import *

urlpatterns = [
    path('', CreateBlog.as_view(), name="create_blog"),
]