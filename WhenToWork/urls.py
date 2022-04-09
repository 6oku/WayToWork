from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from register import views as v
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from .views import cross_off, dashboard, delete, editor, delete_document, todo, uncross, viewPage, timer

urlpatterns = [
    path('notepad/', editor, name='editor'),
    path('delete_document/<int:docid>/', delete_document, name='delete_document'),
    path('admin/', admin.site.urls),
    path('todo/', todo , name="todo"),
    path('delete/<int:list_id>', delete, name = "delete"),
    path('cross_off/<int:list_id>', cross_off, name = "cross_off"),
    path('uncross/<int:list_id>', uncross, name = "uncross"),

    #URLS
    path("register/", v.register, name="register"),
    path('', include("django.contrib.auth.urls")),
    path('', LoginView.as_view(template_name='registration/login.html'), name="login"),
    path('dashboard/', dashboard, name="dashboard"),
    path('view/', viewPage, name="view"),
    path('timer/', timer, name='timer'),
    
    #Reset Password URLS
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]
