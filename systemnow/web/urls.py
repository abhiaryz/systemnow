from django.urls import path
from . import views
urlpatterns = [

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('linux/', views.linux, name='linux'),
    path('linux2/', views.linux2, name='linux2'),
    path('website/', views.website, name='website'),
    path('website_add/', views.website_add, name='website_add'),
    path('website_overview/', views.website_overview, name='website_overview'),
    path('server/', views.server, name='server'),
    path('server_overview/', views.server_overview, name='server_overview'),
    path('server_alert/', views.server_alert, name='server_alert'),
    path('server_cpu/', views.server_cpu, name='server_cpu'),
    path('server_incident/', views.server_incident, name='server_incident'),
    path('server_memory/', views.server_memory, name='server_memory'),
    path('server_from/', views.server_from, name='server_from'),
    path('server_network/', views.server_network, name='server_network'),
    path('server_processes/', views.server_processes, name='server_processes'),
    path('server_storage/', views.server_storage, name='server_storage'),
    path('get_data', views.get_data, name='get_data'),
]
