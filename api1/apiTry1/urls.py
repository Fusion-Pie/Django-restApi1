from django.urls import path
from . import views

urlpatterns = [
    path('v1/gangInfo/', views.gangList),
    path('v1/gangInfo/<int:id>', views.gangInfo),
    path('v1/addGangMember/', views.gangAddMember),
    path('v1/updateGangMember/', views.updateGangMember),
    path('v1/deleteGangMember/<int:id>', views.deleteGangMember),
]