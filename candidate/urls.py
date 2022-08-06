from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('candidateclick', views.candidateclick_view,name='candidateclick'),
    path('candidatesignup', views.candidate_signup_view,name='candidatesignup'),
    path('candidate-dashboard', views.candidate_dashboard_view,name='candidate-dashboard'),
    path('candidatelogin', LoginView.as_view(template_name='conference/adminlogin.html'),name='candidatelogin'),
    path('apply-conference', views.apply_conference_view,name='apply-conference'),
    path('apply/<int:pk>', views.apply_view,name='apply'),
    path('history', views.history_view,name='history'),
    path('categories', views.candidate_category_view,name='category'),
    path('paper', views.paperUpload, name='upload'),
    path('ask-question', views.ask_question_view,name='ask-question'),
    path('apply-conference', views.add_pdf, name='add_pdf'), 
    path('question-history', views.question_history_view,name='question-history'),
]
