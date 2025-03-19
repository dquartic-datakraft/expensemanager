
from django.urls import path # imprt the path function

from . import views # importing views.py which is in same folder

urlpatterns = [
    path('',views.index,name='index'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('login',views.login,name='login'),
    
]
