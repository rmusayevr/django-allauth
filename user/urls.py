from django.urls import path
from .views import login, index

urlpatterns = [
    path('login/', login, name='login'),
    path('', index, name='home'),

]
