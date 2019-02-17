from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('user_owned', views.user_owned, name='users_owned'),
    url('all_owned', views.all_owned, name='all_owned'),
    url('run_rfid', views.Run_rfid, name='Run_rfid'),
    url('run_rf', views.Run_rf, name='Run_rf'),
    url('finger_owned', views.finger_owned, name='finger_owned'),
    url('', views.index, name='users')

]
