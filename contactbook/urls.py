from django .urls import path
from . import views

urlpatterns=[
    path('', views.home , name='home'),
    path('addcontact', views.addContact , name='addcontact'),
    path('profile/<str:pk>', views.Profile , name='profile'),
    path('edit/<str:pk>', views.Edit , name='edit'),
    path('delete/<str:pk>', views.Delete , name='delete'),
]