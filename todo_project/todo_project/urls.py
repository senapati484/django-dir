from django.contrib import admin
from django.urls import path
from todo.views import home,dj, add_task, del_task, update_task
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("dj/", dj, name="dj"),
    path("add/", add_task, name="add_task"),
    path("delete/<int:id>/", del_task, name="del_task"),
    path("update/<int:id>/", update_task, name="update_task")
]
