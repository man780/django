from django.urls import path
from .views import EntityList, EntityDetail, EntityCreate


urlpatterns = [
    path('entity/<int:pk>/', EntityDetail.as_view()),
    path('entity/', EntityList.as_view()),
    path('entity/create/', EntityCreate.as_view()),
]
