from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:task_id>/", views.detail, name="detail"),
    path("update/<int:task_id>/", views.update, name="update"),
]