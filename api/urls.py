from django.urls import path
from .views import EntityList, EntityDetail


urlpatterns = [
    path('<int:pk>/', EntityDetail.as_view()),
    path('', EntityList.as_view()),
]
