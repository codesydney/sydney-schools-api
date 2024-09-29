from django.urls import path
from .views import NSWSchoolList

urlpatterns = [
    path('schools/', NSWSchoolList.as_view(), name='school-list'),
]
