from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('',views.view),
    path('room/',views.room),
    path('get_token/',views.getToken),
    path('create_member/', views.createMember),
    path('get_member/', views.getMember),
    path('delete_member/', views.deleteMember),
    
]