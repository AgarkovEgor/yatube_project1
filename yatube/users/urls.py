from django.contrib.auth.views import LoginView,\
                                    LogoutView, \
                                    PasswordChangeView,\
                                    PasswordChangeDoneView,\
                                    PasswordResetView,\
                                    PasswordResetDoneView,\
                                    PasswordResetConfirmView,\
                                    PasswordResetCompleteView
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path(
        'logout/',
        LogoutView.as_view(template_name='users/logged_out.html'),
        name='logout'
    ),
    path('signup/', views.SignUp.as_view(template_name='users/signup.html'),
         name='signup'),
    path('login/', LoginView.as_view(template_name='users/login.html'),
         name='login'),
    path('password_change/',
         PasswordChangeView.as_view(template_name='users/password_change_form.html'),
         name='password_change_form'),
    path('password_change/done',
         PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name='users/password_reset_form.html'),
         name='password_reset_form'),
    path('password_reset/done',
         PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'),
    path('reset/,<uibd64>/<token>',
         PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm'),
         name='password_reset_confirm'),
    path('reset/done',
         PasswordResetCompleteView.as_view(template_name='users/password_reset_complete'),
         name='password_reset_complete'),
]