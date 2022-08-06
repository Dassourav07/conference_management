from django.shortcuts import render,redirect,reverse
from . import forms,models
from django.db.models import Sum
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required,user_passes_test
from django.conf import settings
from django.db.models import Q
from django.core.mail import send_mail
from django.contrib.auth.models import User
from candidate import models as CMODEL
from candidate import forms as CFORM
from conference.function import handle_uploaded_file
from django.contrib import messages
from django.http import HttpResponse 


def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')  
    return render(request,'conference/index.html')


def is_candidate(user):
    return user.groups.filter(name='CANDIDATE').exists()


def afterlogin_view(request):
    if is_candidate(request.user):      
        return redirect('candidate/candidate-dashboard')
    else:
        return redirect('admin-dashboard')



def adminclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return HttpResponseRedirect('adminlogin')


@login_required(login_url='adminlogin')
def admin_dashboard_view(request):
    dict={
        'total_user':CMODEL.Candidate.objects.all().count(),
        'total_conference':models.Conference.objects.all().count(),
        'total_category':models.Category.objects.all().count(),
        'total_question':models.Question.objects.all().count(),
        'total_conference_holder':models.ConferenceRecord.objects.all().count(),
        'approved_conference_holder':models.ConferenceRecord.objects.all().filter(status='Approved').count(),
        'disapproved_conference_holder':models.ConferenceRecord.objects.all().filter(status='Disapproved').count(),
        'waiting_conference_holder':models.ConferenceRecord.objects.all().filter(status='Pending').count(),
    }
    return render(request,'conference/admin_dashboard.html',context=dict)



@login_required(login_url='adminlogin')
def admin_view_candidate_view(request):
    candidates= CMODEL.Candidate.objects.all()
    return render(request,'conference/admin_view_candidate.html',{'candidates':candidates})



@login_required(login_url='adminlogin')
def update_candidate_view(request,pk):
    candidate=CMODEL.Candidate.objects.get(id=pk)
    user=CMODEL.User.objects.get(id=candidate.user_id)
    userForm=CFORM.CandidateUserForm(instance=user)
    candidateForm=CFORM.CandidateForm(request.FILES,instance=candidate)
    mydict={'userForm':userForm,'candidateForm':candidateForm}
    if request.method=='POST':
        userForm=CFORM.CandidateUserForm(request.POST,instance=user)
        candidateForm=CFORM.CandidateForm(request.POST,request.FILES,instance=candidate)
        if userForm.is_valid() and candidateForm.is_valid():
            user=userForm.save()
            user.set_password(user.password)
            user.save()
            candidateForm.save()
            return redirect('admin-view-candidate')
    return render(request,'conference/update_candidate.html',context=mydict)



@login_required(login_url='adminlogin')
def delete_candidate_view(request,pk):
    candidate=CMODEL.Candidate.objects.get(id=pk)
    user=User.objects.get(id=candidate.user_id)
    user.delete()
    candidate.delete()
    return HttpResponseRedirect('/admin-view-candidate')



def admin_category_view(request):
    return render(request,'conference/admin_category.html')

def admin_add_category_view(request):
    categoryForm=forms.CategoryForm() 
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST)
        if categoryForm.is_valid():
            categoryForm.save()
            return redirect('admin-view-category')
    return render(request,'conference/admin_add_category.html',{'categoryForm':categoryForm})

def admin_view_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'conference/admin_view_category.html',{'categories':categories})

def admin_delete_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'conference/admin_delete_category.html',{'categories':categories})
    
def delete_category_view(request,pk):
    category = models.Category.objects.get(id=pk)
    category.delete()
    return redirect('admin-delete-category')

def admin_update_category_view(request):
    categories = models.Category.objects.all()
    return render(request,'conference/admin_update_category.html',{'categories':categories})

@login_required(login_url='adminlogin')
def update_category_view(request,pk):
    category = models.Category.objects.get(id=pk)
    categoryForm=forms.CategoryForm(instance=category)
    
    if request.method=='POST':
        categoryForm=forms.CategoryForm(request.POST,instance=category)
        
        if categoryForm.is_valid():

            categoryForm.save()
            return redirect('admin-update-category')
    return render(request,'conference/update_category.html',{'categoryForm':categoryForm})
  
  

def admin_conference_view(request):
    return render(request,'conference/admin_conference.html')


def admin_add_conference_view(request):
    conferenceForm=forms.ConferenceForm() 
    
    if request.method=='POST':
        conferenceForm=forms.ConferenceForm(request.POST)
        if conferenceForm.is_valid():
            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            conference = conferenceForm.save(commit=False)
            conference.category=category
            conference.save()
            return redirect('admin-view-conference')
    return render(request,'conference/admin_add_conference.html',{'conferenceForm':conferenceForm})

def admin_view_conference_view(request):
    conferences = models.Conference.objects.all()
    return render(request,'conference/admin_view_conference.html',{'conferences':conferences})



def admin_update_conference_view(request):
    conferences = models.Conference.objects.all()
    return render(request,'conference/admin_update_conference.html',{'conferences':conferences})

@login_required(login_url='adminlogin')
def update_conference_view(request,pk):
    conference = models.Conference.objects.get(id=pk)
    conferenceForm=forms.ConferenceForm(instance=conference)
    
    if request.method=='POST':
        conferenceForm=forms.ConferenceForm(request.POST,instance=conference)
        
        if conferenceForm.is_valid():

            categoryid = request.POST.get('category')
            category = models.Category.objects.get(id=categoryid)
            
            conference = conferenceForm.save(commit=False)
            conference.category=category
            conference.save()
           
            return redirect('admin-update-conference')
    return render(request,'conference/update_conference.html',{'conferenceForm':conferenceForm})
  
  
def admin_delete_conference_view(request):
    conferences = models.Conference.objects.all()
    return render(request,'conference/admin_delete_conference.html',{'conferences':conferences})
    
def delete_conference_view(request,pk):
    conference = models.Conference.objects.get(id=pk)
    conference.delete()
    return redirect('admin-delete-conference')

def admin_view_conference_holder_view(request):
    conferencerecords = models.ConferenceRecord.objects.all()
    return render(request,'conference/admin_view_conference_holder.html',{'conferencerecords':conferencerecords})

def admin_view_approved_conference_holder_view(request):
    conferencerecords = models.ConferenceRecord.objects.all().filter(status='Approved')
    return render(request,'conference/admin_view_approved_conference_holder.html',{'conferencerecords':conferencerecords})

def admin_view_disapproved_conference_holder_view(request):
    conferencerecords = models.ConferenceRecord.objects.all().filter(status='Disapproved')
    return render(request,'conference/admin_view_disapproved_conference_holder.html',{'conferencerecords':conferencerecords})

def admin_view_waiting_conference_holder_view(request):
    conferencerecords = models.ConferenceRecord.objects.all().filter(status='Pending')
    return render(request,'conference/admin_view_waiting_conference_holder.html',{'conferencerecords':conferencerecords})

def approve_request_view(request,pk):
    conferencerecords = models.ConferenceRecord.objects.get(id=pk)
    conferencerecords.status='Approved'
    conferencerecords.save()
    return redirect('admin-view-conference-holder')

def disapprove_request_view(request,pk):
    conferencerecords = models.ConferenceRecord.objects.get(id=pk)
    conferencerecords.status='Disapproved'
    conferencerecords.save()
    return redirect('admin-view-conference-holder')


def admin_question_view(request):
    questions = models.Question.objects.all()
    return render(request,'conference/admin_question.html',{'questions':questions})

def update_question_view(request,pk):
    question = models.Question.objects.get(id=pk)
    questionForm=forms.QuestionForm(instance=question)
    
    if request.method=='POST':
        questionForm=forms.QuestionForm(request.POST,instance=question)
        
        if questionForm.is_valid():

            admin_comment = request.POST.get('admin_comment')
            
            
            question = questionForm.save(commit=False)
            question.admin_comment=admin_comment
            question.save()
           
            return redirect('admin-question')
    return render(request,'conference/update_question.html',{'questionForm':questionForm})







def aboutus_view(request):
    return render(request,'conference/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message,settings.EMAIL_HOST_USER, settings.EMAIL_RECEIVING_USER, fail_silently = False)
            return render(request, 'conference/contactussuccess.html')
    return render(request, 'conference/contactus.html', {'form':sub})


def uploadForm(request):
    	return render(request, 'conference/contactus.html')


def add_pdf(request):
    if request.method == 'POST':
        file = request.FILES['pdf']  
        file.save() 
        handle_uploaded_file(request.FILES['file'])  
        return HttpResponse("File uploaded successfuly")  
    else:
        messages.error(request, 'Files was not Submitted successfully')
        return redirect('apply-conference')


