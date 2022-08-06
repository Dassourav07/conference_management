from django.shortcuts import render,redirect,reverse
from django.core.files.storage import FileSystemStorage
import conference
from . import forms,models
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.mail import send_mail
from conference import models as CMODEL
from conference import forms as CFORM
from django.views import generic
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse 
from candidate.forms import candidateForm
from candidate.function import handle_uploaded_file

 

 

def candidateclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'candidate/candidateclick.html')


def candidate_signup_view(request):
    userForm=forms.CandidateUserForm()
    candidateForm=forms.CandidateForm()
    mydict={'userForm':userForm,'candidateForm':candidateForm}
    if request.method=='POST':
        userForm=forms.CandidateUserForm(request.POST)
        candidateForm=forms.CandidateForm(request.POST,request.FILES)
        if userForm.is_valid() and candidateForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            candidate=candidateForm.save(commit=False)
            candidate.user=user
            candidate.save()
            my_candidate_group = Group.objects.get_or_create(name='CANDIDATE')
            my_candidate_group[0].user_set.add(user)
        return HttpResponseRedirect('candidatelogin')
    return render(request,'candidate/candidatesignup.html',context=mydict)

def is_candidate(user):
    return user.groups.filter(name='candidate').exists()

@login_required(login_url='candidatelogin')
def candidate_dashboard_view(request):
    dict={
        'candidate':models.Candidate.objects.get(user_id=request.user.id),
        'available_conference':CMODEL.Conference.objects.all().count(),
        'applied_conference':CMODEL.ConferenceRecord.objects.all().filter(candidate=models.Candidate.objects.get(user_id=request.user.id)).count(),
        'total_category':CMODEL.Category.objects.all().count(),
        'total_question':CMODEL.Question.objects.all().filter(candidate=models.Candidate.objects.get(user_id=request.user.id)).count(),
    
    } 
    return render(request,'candidate/candidate_dashboard.html',context=dict)

def apply_conference_view(request):
    candidate = models.Candidate.objects.get(user_id=request.user.id)
    conferences = CMODEL.Conference.objects.all()
    return render(request,'candidate/apply_conference.html',{'conferences':conferences,'candidate':candidate})

def apply_view(request,pk):
    candidate = models.Candidate.objects.get(user_id=request.user.id)
    conference = CMODEL.Conference.objects.get(id=pk)
    conferencerecord = CMODEL.ConferenceRecord()
    conferencerecord.conference = conference
    conferencerecord.candidate = candidate
    conferencerecord.save()
    return redirect('history')

def history_view(request):
    candidate = models.Candidate.objects.get(user_id=request.user.id)
    conferences = CMODEL.ConferenceRecord.objects.all().filter(candidate=candidate)
    return render(request,'candidate/history.html',{'conferences':conferences,'candidate':candidate})

def candidate_category_view(request):
    return render(request,'candidate/apply_conference.html')

def ask_question_view(request):
    candidate = models.Candidate.objects.get(user_id=request.user.id)
    questionForm=CFORM.QuestionForm() 
    
    if request.method=='POST':
        questionForm=CFORM.QuestionForm(request.POST)
        if questionForm.is_valid():
            
            question = questionForm.save(commit=False)
            question.candidate=candidate
            question.save()
            return redirect('question-history')
    return render(request,'candidate/ask_question.html',{'questionForm':questionForm,'candidate':candidate})

def question_history_view(request):
    candidate = models.Candidate.objects.get(user_id=request.user.id)
    questions = CMODEL.Question.objects.all().filter(candidate=candidate)
    return render(request,'candidate/question_history.html',{'questions':questions,'candidate':candidate})


@login_required
def paperUpload(request):
    if request.method == 'POST':
        file = request.FILES['pdf']  
        file.save() 
        handle_uploaded_file(request.FILES['file'])  
        return HttpResponse("File uploaded successfuly")  
    else:
        messages.error(request, 'Files was not Submitted successfully')
        return redirect('apply-conference')

def add_pdf(request):
    if request.method == 'POST':
        file = request.FILES['pdf']  
        file.save() 
        handle_uploaded_file(request.FILES['file'])  
        return HttpResponse("File uploaded successfuly")  
    else:
        messages.error(request, 'Files was not Submitted successfully')
        return redirect('apply-conference')