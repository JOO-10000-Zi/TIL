from django.urls import path
from . import views

app_name = 'articles'

urlpatterns=[
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('addreview', views.addreview, name='addreview'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('edit/<int:pk>', views.edit, name='edit'),
]