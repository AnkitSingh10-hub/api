from django.urls import path, include
from . import views
urlpatterns = [

    path('api/employees', views.employeeListView),
    path('api/users', views.UserListView),
    path('api/employees/<int:pk>', views.employeeDetailView),

]
