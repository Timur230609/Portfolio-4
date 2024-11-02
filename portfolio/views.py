from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def contact_view(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            content = request.POST.get('content')
            new_contact = Contact(name=name, email=email, content=content)
            new_contact.save()
            messages.success(request, "Your message was successfully sent!")
            return redirect('home-page')  # Bu yerda HttpResponseRedirect o'rniga redirect() ishlatilmoqda
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('contact')
    
    return render(request, 'contact.html')



def index_view(request):
 return render(request,'index.html')

def bloggrid_view(request):
 return render(request,'blog_grid.html')

def blog_view(request):
 return render(request,'blog.html')

def services_view(request):
 return render(request,'service.html')

def about_view(request):
 return render(request,'about.html')

def blogdetail_view(request):
 return render(request,'blog_detail.html')

def career_view(request):
 return render(request,'career.html')

def cart_view(request):
 return render(request,'cart.html')

def checkout_view(request):
 return render(request,'checkout.html')

def comprepair_view(request):
 return render(request,'computer_repair.html')

def contact_2_view(request):
    return render(request, 'contact_2.html')

def datarec_view(request):
    return render(request, 'data_recovery.html')

def error_view(request):
    return render(request, 'error.html')

def faq_view(request):
    return render(request, 'faq.html')

def homedark_view(request):
    return render(request, 'home_dark.html')

def home_view(request):
    return render(request, 'home.html')

def make_view(request):
    return render(request, 'make_appointment.html')

def mobileserver_view(request):
    return render(request, 'mobile_service.html')

def network_view(request):
    return render(request, 'network_solution.html')

def news_view(request):
    return render(request, 'news.html')

def price_view(request):
    return render(request, 'price.html')

def policy_view(request):
    return render(request, '.html')

def _view(request):
    return render(request, 'privacy_policy.html')

def servicedetal_view(request):
    return render(request, 'service_detail.html')


def servicelist_view(request):
    return render(request, 'service_list.html')

def service_view(request):
    return render(request, 'service.html')

def shopdetal_view(request):
   return render(request, 'shop_detail.html')

def shop_view(request):
   return render(request, 'shop.html')

def tech_view(request):
   return render(request, 'techn_support.html')

def term_view(request):
   return render(request, 'term_condition.html')