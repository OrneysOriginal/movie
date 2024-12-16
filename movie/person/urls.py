from django.urls import path

from person.views import LoginView, RegistrationView, LogoutView, ProfileView

app_name = "person"

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
]
