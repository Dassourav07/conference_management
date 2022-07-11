from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('candidateclick', views.candidateclick_view,name='candidateclick'),
    path('candidatesignup', views.candidate_signup_view,name='candidatesignup'),
    path('candidate-dashboard', views.candidate_dashboard_view,name='candidate-dashboard'),
    path('candidatelogin', LoginView.as_view(template_name='conference/adminlogin.html'),name='candidatelogin'),
    path('apply-policy', views.apply_policy_view,name='apply-policy'),
    path('apply/<int:pk>', views.apply_view,name='apply'),
    path('history', views.history_view,name='history'),

    path('ask-question', views.ask_question_view,name='ask-question'),
    path('question-history', views.question_history_view,name='question-history'),
]