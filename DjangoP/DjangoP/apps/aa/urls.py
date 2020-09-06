from django.urls import path
from . import views
app_name = 'aa'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:arti_id>/', views.detail, name='detail'),
    path('<int:arti_id>/leave_comm/', views.leave_comm, name='leave_comm')
]