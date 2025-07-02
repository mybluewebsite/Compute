from django.urls import path
from . import views

app_name = 'myapp' # Namespace for URLs, e.g., {% url 'myapp:home' %}

urlpatterns = [
    path('', views.home, name='home'), # Example home page
    # path('about/', views.about, name='about'), # Another example
]