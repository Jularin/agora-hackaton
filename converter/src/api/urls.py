from django.urls import path

from api.views import UploadData

urlpatterns = [
    path('upload/', UploadData.as_view()),
]
