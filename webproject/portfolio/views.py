from django.shortcuts import render, redirect
from .models import Education, Experience, Skill, Product, Contact, OwnerInfo

def home(request):
    owner_info = OwnerInfo.objects.first()  # Assuming there's only one owner's info
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    skills = Skill.objects.all()
    products = Product.objects.all()
    context = {
        'owner_info': owner_info,
        'educations': educations,
        'experiences': experiences,
        'skills': skills,
        'products': products,
    }
    return render(request, 'portfolio/home.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            try:
                Contact.objects.create(name=name, email=email, message=message)
                return redirect('home')
            except Exception as e:
                print(f"Error: {e}")
    return render(request, 'contact.html')
