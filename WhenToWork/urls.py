from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from register import views as v
from .views import cross_off, dashboard, delete, editor, delete_document, todo, uncross, viewPage

urlpatterns = [
    path('notepad/', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    path('admin/', admin.site.urls),
    path('todo/', todo , name="todo"),
    path('delete/<int:list_id>', delete, name = "delete"),
    path('cross_off/<int:list_id>', cross_off, name = "cross_off"),
    path('uncross/<int:list_id>', uncross, name = "uncross"),
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('dashboard/', dashboard, name="dashboard"),
    path('view/', viewPage, name="view"),

]

