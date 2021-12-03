from . import views
from django.urls import path

urlpatterns = [

    path('', views.page2, name='page2'),
    path('aa',views.data,name='aa'),
    path('congratulation',views.congratulation,name='congratulation'),


]
