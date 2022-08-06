
from django.contrib import admin
from django.urls import path
from conference import views
from django.contrib.auth.views import LogoutView,LoginView
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('candidate/',include('candidate.urls')),
    path('',views.home_view,name=''),
    path('logout/', LogoutView.as_view(template_name='conference/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('apply-conference', views.add_pdf, name='add_pdf'), 
    
    path('adminlogin', LoginView.as_view(template_name='conference/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('admin-view-candidate', views.admin_view_candidate_view,name='admin-view-candidate'),
    path('update-candidate/<int:pk>', views.update_candidate_view,name='update-candidate'),
    path('delete-candidate/<int:pk>', views.delete_candidate_view,name='delete-candidate'),

    path('admin-category', views.admin_category_view,name='admin-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),


    path('admin-conference', views.admin_conference_view,name='admin-conference'),
    path('admin-add-conference', views.admin_add_conference_view,name='admin-add-conference'),
    path('admin-view-conference', views.admin_view_conference_view,name='admin-view-conference'),
    path('admin-update-conference', views.admin_update_conference_view,name='admin-update-conference'),
    path('update-conference/<int:pk>', views.update_conference_view,name='update-conference'),
    path('admin-delete-conference', views.admin_delete_conference_view,name='admin-delete-conference'),
    path('delete-conference/<int:pk>', views.delete_conference_view,name='delete-conference'),

    path('admin-view-conference-holder', views.admin_view_conference_holder_view,name='admin-view-conference-holder'),
    path('admin-view-approved-conference-holder', views.admin_view_approved_conference_holder_view,name='admin-view-approved-conference-holder'),
    path('admin-view-disapproved-conference-holder', views.admin_view_disapproved_conference_holder_view,name='admin-view-disapproved-conference-holder'),
    path('admin-view-waiting-conference-holder', views.admin_view_waiting_conference_holder_view,name='admin-view-waiting-conference-holder'),
    path('approve-request/<int:pk>', views.approve_request_view,name='approve-request'),
    path('reject-request/<int:pk>', views.disapprove_request_view,name='reject-request'),

    path('admin-question', views.admin_question_view,name='admin-question'),
    path('update-question/<int:pk>', views.update_question_view,name='update-question'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

