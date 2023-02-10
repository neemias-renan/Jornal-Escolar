from django.urls import path
from . import views

app_name = 'inrite'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('news/<int:pk>', views.NewsView.as_view(), name='new'),
    path('manager/', views.ManagerView.as_view(), name='manager'),
]