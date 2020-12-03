from django.urls import path,include
from .views import WelcomeView

app_name='blog'

urlpatterns = [
    path('',WelcomeView.as_view()),

]
