
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render
from .forms import *
from .models import *

def index(request):
    total = Total.objects.all()
    testimonials = Testimonials.objects.all()
    skills = Skills.objects.all()
    details = Mydetails.objects.all()
    services = Services.objects.all()
    portfolio = Portfolio.objects.all()
    portfolio_category = CategoryTitle.objects.all()
    resume = Resume.objects.all()
    about = About.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            print(name, email, subject)

            # Customize this part with your own email settings
            send_mail(
                name,
                f'From: {name} <{email}>\n\n{message}',
                'settings.EMAIL_HOST_USER',
                [email],  # Change to the specific email address
                fail_silently=False
            )

            # Redirect or display success message after sending the email
            return render(request, 'index.html')  # Replace 'success.html' with your success page

    else:
        form = ContactForm()

    return render(request, 'index.html', {
        'form': form,
        'total': total,
        'testimonials': testimonials,
        'skills': skills,
        'details': details,
        'services': services,
        'portfolio': portfolio,
        'portfolio_category': portfolio_category,
        'resume': resume,
        'about': about
    })



# def index(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             print(name, email, subject)

#             # Customize this part with your own email settings
#             send_mail(
#             name,
#             message, 
#             subject,
#             'settings.EMAIL_HOST_USER',
#             [email]

#             )


#             # Redirect or display success message after sending the email
#             return render(request, '#contact')
#             total = Total.objects.all()
#             testimonials = Testimonials.objects.all()
#             skills = Skills.objects.all()
#             details = Mydetails.objects.all()
#             services = Services.objects.all()
#             portfolio = Portfolio.objects.all()
#             portfolio_category = CategoryTitle.objects.all()
#             resume = Resume.objects.all()
#             about = About.objects.all()
#             print(total)
#             print(testimonials)
#             print(skills)
#             print(details)
#             print(skills)
#             print(services)
#             print(portfolio)
#             print(portfolio_category)
#             print(resume)
#             print(about)
#     else:
#         form = ContactForm()

#     return render(request, 'index.html', {'form': form, 'total':total, 'testimonials':testimonials,
#      'skills':skills, 'details':details, 'services':services, 'portfolio':portfolio,
#       'portfolio_category':portfolio_category, 'resume':resume, 'about':about})



# def index(request):
#     total = Total.objects.all()
#     testimonials = Testimonials.objects.all()
#     skills = Skills.objects.all()
#     details = Mydetails.objects.all()
#     services = Services.objects.all()
#     portfolio = Portfolio.objects.all()
#     portfolio_category = CategoryTitle.objects.all()
#     resume = Resume.objects.all()
#     about = About.objects.all()
#     print(total)
#     print(testimonials)
#     print(skills)
#     print(details)
#     print(skills)
#     print(services)
#     print(portfolio)
#     print(portfolio_category)
#     print(resume)
#     print(about)
#     return render(request, 'index.html', {'total':total, 'testimonials':testimonials,
#      'skills':skills, 'details':details, 'services':services, 'portfolio':portfolio,
#       'portfolio_category':portfolio_category, 'resume':resume, 'about':about

#       }
#     )


def portfoliodetails(request, portfolio_id):
    portfolio = Portfolio.objects.get(id=portfolio_id)

    return render(request, 'portfolio-details.html', {'portfolio':portfolio})


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")