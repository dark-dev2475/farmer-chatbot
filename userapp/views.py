from django.shortcuts import render,redirect
from userapp.models import *
import pyttsx3
from textblob import TextBlob
from django.contrib import messages


def main_user_login(req):
          
          if req.method == 'POST':
                    email = req.POST.get('email')
                    password = req.POST.get('password')
                    
                    try:
                              user = User.objects.get(
                              user_email=email, user_password=password)
                              req.session['user_id'] = user.user_id
                              if user.user_status == 'Accepted':
                                        engine = pyttsx3.init()
                                        print(user.user_fullname)
                                        engine. setProperty("rate", 110) 
                                        engine.say("welcome {}".format(user.user_fullname))
                                        engine.runAndWait()
                                        messages.success(req, 'Successfully Login')
                                        return redirect('user_dashboard')
                              elif user.user_status == 'Pending':
                                        messages.warning(req, 'Your request is in pending, please wait for until acceptance')
                                        return redirect('user_login')
                              elif user.user_status == 'Restricted':
                                        messages.warning(req, 'Your request is Restricted, so you cannot login')
                                        return redirect('user_login')          
                              elif user.user_status == 'Rejected':
                                        messages.error(req, 'Your request is rejected, so you cannot login')
                                        return redirect('user_login')
                                        
                    except:
                              print('hi')
                              messages.warning(req, 'invalid login')
                              return redirect('user_login')
                              
          return render (req,'main/main-user-login.html' )

def main_user_register(req):
          if req.method == 'POST' and req.FILES["pic"]:
                    fullname = req.POST.get("fullname")
                    username = req.POST.get("username")
                    email = req.POST.get("email")
                    password = req.POST.get("password")
                    contact = req.POST.get("contact")
                    city = req.POST.get("city")
                    state = req.POST.get("state")
                    image = req.FILES["pic"]
                    User.objects.create(user_fullname=fullname , user_username=username , user_email=email , user_password=password , user_contact=contact , user_city=city , user_state=state , user_image=image)
                    messages.success(req, 'Successfully Registered. Wait For Approval')
                    
                    
          return render (req,'main/main-user-register.html' )

def user_dashboard(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          # importing the pyttsx library


          return render (req,'user/user-dashboard.html' )

def user_chatbot_btn(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          return render (req,'user/user-chatbot-btn.html' )

def user_chatbot(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          return render (req,'user/user-chatbot.html' )

def user_myprofile(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          
        
          return render (req,'user/user-profile.html',{'user':user})

def user_edit_profile(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          if req.method == 'POST':
                    fullname = req.POST.get("fullname")
                    username = req.POST.get("username")
                    email = req.POST.get("email")
                    contact = req.POST.get("contact")
                    city = req.POST.get("city")
                    state = req.POST.get("state")
                    print(fullname,'hiii')
                    if len(req.FILES) != 0:
                              image = req.FILES["image"]
                              user.user_fullname = fullname
                              user.user_username = username
                         
                              user.user_contact = contact
                              user.user_city = city
                              user.user_state = state
                              user.user_image = image
                              user.save()
                              messages.success(req,'Updated Successfully')
                    else:
                              user.user_fullname = fullname
                              user.user_username = username
                              
                              user.user_contact = contact
                              user.user_city = city
                              user.user_state = state
                              user.save()
                              messages.success(req,'Updated Successfully')
                    
                              
                    return redirect('user_edit_profile')
          return render (req,'user/user-edit-myprofile.html',{'user':user})

def user_password(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          if req.method == 'POST':
                password = req.POST.get('password')
                npassword = req.POST.get('npassword')
                cpassword = req.POST.get('cpassword')
                
                if password == user.user_password:
                          print('old password is equal')
                          if npassword == cpassword:
                                    user.user_password = cpassword
                                    user.save()
                                    messages.success(req,'Password Updated Successfully')
                                    return redirect('user_password')
                          else:
                                    messages.warning(req,'New Password and Confirm New Password Should Match')

                else:
                          messages.warning(req,'Old Password and Current Password Should Match')
                    
          return render (req,'user/user-change-password.html' )

def user_cropdetails(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          return render (req,'user/user-cropdetails.html' )

def user_fertilizer(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          return render (req,'user/user-fertilizer.html' )

def user_feedback(req):
          user_id = req.session['user_id']
          user = User.objects.get(user_id=user_id)
          if req.method == 'POST' :
                    
                    desc = req.POST.get("feedback")
                    rating = req.POST.get("rating")
                    print(desc, rating)
                    user_id = req.session['user_id']
                    user = User.objects.get(pk=user_id)
                    if not rating:
                              messages.info(req, 'Please Give rating')            
                              return redirect('user_feedback')
                    analysis = TextBlob(desc)
                    senti = ''
                    if analysis.polarity >= 0.5:
                              senti = 'Very Positive'
                    elif analysis.polarity > 0 and analysis.polarity < 0.5:
                              senti = 'Positive'
                    elif analysis.polarity < 0 and analysis.polarity >= -0.5:
                              senti = 'Negative'
                    elif analysis.polarity < -0.5:
                              senti = 'Very Negative'
                    else:
                              senti = 'Neutral'
                    print(senti, 'sentiment')
                    print(desc)
                    Feedback.objects.create(feed_desc=desc, feed_rating=rating,feedback_sentiment=senti,feedback_user=user)
                    messages.success(req,'Feedback Submitted')
          return render (req,'user/user-feedback.html' )