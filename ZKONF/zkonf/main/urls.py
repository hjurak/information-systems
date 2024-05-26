from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('conference/<int:conference_id>/', views.conference_detail, name='conference_detail'),
    path('participant/<int:participant_id>/', views.participant_detail, name='participant_detail'),
    path('scientific_work/<int:work_id>/', views.scientific_work_detail, name='scientific_work_detail'),
    path('works/', views.work_list, name='work_list'),
    path('search/', views.search, name='search'),
    path('search_by_title/', views.search_by_title, name='search_by_title'),
    path('search_by_participant/', views.search_by_participant, name='search_by_participant'),

        # Participant URLs
    path('participants/', views.participant_list, name='participant_list'),
    path('participants/<int:pk>/', views.participants_detail, name='participants_detail'),
    path('participants/create/', views.participant_create, name='participant_create'),
    path('participants/<int:pk>/update/', views.participant_update, name='participant_update'),
    path('participants/<int:pk>/delete/', views.participant_delete, name='participant_delete'),

    # ScientificWork URLs
    path('scientificworks/', views.scientificwork_list, name='scientificwork_list'),
    path('scientificworks/<int:pk>/', views.scientificwork_detail, name='scientificwork_detail'),
    path('scientificworks/create/', views.scientificwork_create, name='scientificwork_create'),
    path('scientificworks/<int:pk>/update/', views.scientificwork_update, name='scientificwork_update'),
    path('scientificworks/<int:pk>/delete/', views.scientificwork_delete, name='scientificwork_delete'),
]
