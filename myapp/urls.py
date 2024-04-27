from django.urls import path
from .views import *  # Import specific views

urlpatterns = [
    path('', index, name='homepage'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('design/', design, name='design'),
    path('mydesign/', mydesign, name='mydesign'),
    path('signup/', signup, name='signup'),  # Adjust the path for signup
    path("registration_view/", registration_view, name='registration_view'),
    path("login_view/", login_view, name='login_view'),
    path('feedback/', feedback_view, name='feedback'),
    path('thank-you/', thank_you_view, name='thank_you'),
    path('admin_home',admin_home,name='admin_home'),
    # Other URL patterns
]