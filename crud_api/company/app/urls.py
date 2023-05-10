from django.urls import path
from app.views import StudentApiView




urlpatterns = [
    path('student/', StudentApiView.as_view(), name='student'),
]