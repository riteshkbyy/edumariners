from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def home(request):
    context = {
        'section_name': Section.objects.all()
    }
    return render(request, 'edumariners/home.html', context, {'title' : 'Home'})


def about(request):
    return render(request, 'edumariners/contact.html', {'title': 'About'})


def mes(request):
    context = {
        'subject_name': Subject.objects.all()
    }
    return render(request, 'edumariners/mes.html', context)


def iq(request):
    return render(request, 'edumariners/iq.html', {'title': 'interview questions'})


def imuexam(request):
    return render(request, 'edumariners/imuexam.html', {'title': 'Indian Maritime University Exam'})


def career(request):
    return render(request, 'edumariners/career.html', {'title': 'career at sea'})


def news(request):
    return render(request, 'edumariners/news.html', {'title': 'Maritime News'})


def docs(request, subject_id):

    context = {
        'topic_name': Topic.objects.filter(subject_id=subject_id)
    }
    return render(request, 'edumariners/docs.html', context)


def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['ritesh@yadav.ind.in'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "edumariners/contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')






