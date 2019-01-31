from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.HomePage, name="home_page"),
    path('post/<str:title>', views.post_detail, name="post_detail")
]