from django.urls import path
from erp_receiver import views
from erp_receiver.views import DownloadData

urlpatterns = [
    path("test", views.hello_world, name="hello_world"),
    path("download/", DownloadData.as_view(), name="download_data"),
]
