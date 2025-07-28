

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from django.conf.urls import include


urlpatterns = [
    path('', views.home_view),
    path('adminclick', views.adminclick_view),
    path('adminsignup', views.adminsignup_view),
    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view),
    path('updatebook/<int:id>/',views.updatebook_view, name='updatebook'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    
]
