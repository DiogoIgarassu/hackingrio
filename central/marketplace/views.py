from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):

    services = Service.objects.all()
    context = {'services': services}
    template_name = 'marketplace/home.html'

    return render(request, template_name, context)

'''
@login_required
@enrollment_required
def announcements(request, slug):
    course = request.course
    templates = 'courses/announcements.html'
    context = {
            'course': course,
            'announcements': course.announcements.all()
        }
    return render(request, templates, context)

@login_required
@enrollment_required
def show_comments(request, slug, pk):
    course = request.course
    announcement = get_object_or_404(course.announcements.all(), pk=pk)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        print(comment.user)
        comment.announcement = announcement
        print(comment.announcement)
        comment.save()
        form = CommentForm()
        messages.success(request, 'Seu comentário foi enviado com sucesso')
    templates = 'courses/show_announcement.html'
    context = {
        'course': course,
        'announcement': announcement,
        'form': form
    }
    return render(request, templates, context)

'''