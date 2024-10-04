from django.urls import path
from .views import ThreadList, ThreadDetail, add_message, star_thread

messenger_patterns = ([
    path('', ThreadList.as_view(), name="list"),
    path('thread/<int:pk>/', ThreadDetail.as_view(), name="detail"),
    path('thread/<int:pk>/add/', add_message, name="add"),
    path('thread/start/<username>/', star_thread, name="start"),
], "messenger") 