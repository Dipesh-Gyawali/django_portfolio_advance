from django.shortcuts import render
from .models import Home, About, Profile, Category, Portfolio, Contactform
# Create your views here.

def index(request):
    
    # Home
    home = Home.objects.latest('updated')
    
    # About
    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)
    
    # Skills
    categories = Category.objects.all()
    
    # Portfolio
    portfolios = Portfolio.objects.all()
    
    # Contact Form
    if request.method=="POST":
        n_name=request.POST.get("n_name","")
        email=request.POST.get("email","")
        description=request.POST.get("description","")
        
        contact = Contactform(n_name=n_name, email=email, description =description)
        contact.save()
    
    
    context = {
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
    }
    return render(request,'index.html',context)