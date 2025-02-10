from django.shortcuts import render,get_object_or_404,redirect
from userapp.models import *
from django.contrib import messages
import requests
import json
from django.db.models.query import Q
from django.core.paginator import Paginator



def main_admin(req):
          if req.method == "POST":
                    username=req.POST.get("username")
                    password=req.POST.get("password")
                    if username == "admin" and password == "admin":
                              messages.success(req,'Successfully Login')
                              return redirect('admin_dashboard')
                    else:
                              messages.warning(req,'invalid login')
                              return redirect("admin_login")
          return render (req,'main/main-admin.html' )


def admin_dashboard(req):
          users = User.objects.all().count()
          pending = User.objects.filter(user_status='Pending').count()
          restrict = User.objects.filter(user_status='Restricted').count()
          context = {'i':users,'j':pending,'k':restrict}
          return render (req,'admin/admin-dashboard.html',context )

def admin_pending(req):
    
    restrict=User.objects.filter(user_status='Pending').order_by('-user_id')
    
   
    paginator = Paginator(restrict, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render (req,'admin/admin-pending.html',{'restrict':post} )



def accept_users(req,user_id):
    accept = get_object_or_404(User,user_id=user_id)
    accept.user_status ="Accepted"
    accept.save(update_fields=["user_status"])
    accept.save()
    messages.success(req,'User Accepted')
    user = User.objects.get(user_id=user_id)
    url = "https://www.fast2sms.com/dev/bulkV2"
    message = 'Admin Has Accepted Your Request Now You Can Login'
    numbers = user.user_contact
    payload = f'sender_id=FTWSMS&message={message}&language=english&route=v3&numbers={numbers}'
    headers = {
    'authorization': "xZIssgvbBl4hSeai7mMebAMxcusK4BbhQZGO3v1O0ZlAUjuRFWhLAR5hA2SK",
    'Content-Type': "application/json",
    'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text,'heloooooo')
    return redirect('admin_pending')



def reject_users(req,user_id):
    reject = get_object_or_404(User,user_id=user_id)
    reject.user_status ="Rejected"
    reject.save(update_fields=["user_status"])
    reject.save()
    messages.error(req,'User Rejected')
    return redirect('admin_pending')




def admin_all_user(req):
    
          
    restrict = User.objects.filter(Q(user_status='Accepted')|Q(user_status='Restricted')).order_by('-user_id').exclude(user_status='Pending')

    
   
    paginator = Paginator(restrict, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render (req,'admin/admin-all-user.html',{'restrict':post} )


def change_status_users(req,user_id):
    change_status = get_object_or_404(User,user_id=user_id)
    if change_status.user_status == 'Accepted':
        change_status.user_status ="Restricted"
        messages.warning(req,'User Restricted')
    else:
        change_status.user_status ="Accepted"
        messages.success(req,'User Approved')
          
    change_status.save(update_fields=["user_status"])
    change_status.save()
    return redirect('admin_all_user')

def remove_users(req,user_id):
    remove = get_object_or_404(User,user_id=user_id)
    remove.delete()
    messages.error(req,'User Terminated')
    return redirect('admin_all_user')



def admin_user_profile(req):
    
    restrict=User.objects.filter(user_status='Accepted').order_by('-user_id')
    
   
    paginator = Paginator(restrict, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
    return render (req,'admin/admin-user-profile.html',{'restrict':post} )

def admin_user_profile_view(req,user_id):
          profile = User.objects.get(user_id=user_id)
          return render (req,'admin/admin-user-profile-view.html',{'profile':profile} )

def admin_feedback(req):
          
    restrict= Feedback.objects.all().order_by('-feed_id')
    
   
    paginator = Paginator(restrict, 5)
    page_number = req.GET.get('page')
    post = paginator.get_page(page_number)
          
    return render (req,'admin/admin-feedback.html',{'feedback':post} )

def admin_feedback_graph(req):
          very_positive = Feedback.objects.filter(feedback_sentiment='Very Positive').count()
          positive = Feedback.objects.filter(feedback_sentiment='Positive').count()
          neutral = Feedback.objects.filter(feedback_sentiment='Neutral').count()
          negative = Feedback.objects.filter(feedback_sentiment='Negative').count()
          very_negative = Feedback.objects.filter(feedback_sentiment='Very Negative').count()
    
          return render (req,'admin/admin-feedback-graph.html',{
              'i':very_positive,
              'j':positive,
              'k':neutral,
              'l':negative,
              'm':very_negative,
              
          } )
