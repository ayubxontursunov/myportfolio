from django.shortcuts import render, redirect
from .models import Comment
from django.conf import settings



# Create your views here.
def home_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        text = request.POST.get('comment')

        comment = Comment(name=name, email=email, subject=subject, text=text)
        comment.save()
        redirect('https://github.com/ayubxontursunov')

    return render(request, "index.html")

# def project_view(request):
#     return render(request, "project.html")
#
#
# def projects(request):
#     return render(request, "project-cards.html")



