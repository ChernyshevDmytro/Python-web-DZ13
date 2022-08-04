from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('records/', views.records, name='records'),
    path('delete/<int:id>', views.delete_record, name='delete_record'),
    path('details', views.main, name='main'),
]