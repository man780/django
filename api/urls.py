from django.urls import path
from .views import EntityList, EntityDetail, EntityCreate, EntityFullList


urlpatterns = [
    path('entity/<int:pk>/', EntityDetail.as_view()),
    path('entity/', EntityList.as_view()),
    path('entity/full/', EntityFullList.as_view()),
    path('entity/create/', EntityCreate.as_view()),
]
