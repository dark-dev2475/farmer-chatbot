from django.shortcuts import render

def main_home(req):
          return render (req,'main/main-home.html' )

def main_about(req):
          return render (req,'main/main-about.html' )

def main_contact(req):
          return render (req,'main/main-contact.html' )

